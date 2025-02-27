def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_primes = []
    for num in numbers:
        if str(num).count('0') > 0:
            continue
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num) or not is_prime(num):
                break
            num = temp_num
        else:
            left_right_primes.append(num)
    return sorted(set(left_right_primes), reverse=True)