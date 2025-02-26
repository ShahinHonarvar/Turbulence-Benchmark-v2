def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[758]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        is_truncatable = True
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                is_truncatable = False
                break
            temp_num //= 10
        if not is_truncatable:
            continue
        temp_num = num
        while temp_num > 0:
            if not is_prime(temp_num):
                is_truncatable = False
                break
            temp_num = int(str(temp_num)[1:])
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)