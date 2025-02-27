def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for num in numbers:
        if num < 10:
            continue
        left_truncatable = True
        right_truncatable = True
        temp_num = num
        while temp_num > 9:
            if not is_prime(temp_num):
                left_truncatable = False
                break
            temp_num = temp_num // 10
        temp_num = num
        while temp_num > 9:
            if not is_prime(temp_num):
                right_truncatable = False
                break
            temp_num = temp_num % 10 ** (len(str(temp_num)) - 1)
        if left_truncatable and right_truncatable and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)