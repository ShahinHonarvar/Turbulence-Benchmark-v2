def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[74]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            temp_num = num
            while temp_num > 0:
                temp_num //= 10
                if temp_num > 0 and (not is_prime(temp_num)):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)