def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[792]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num)):
                if not is_prime(int(str_num[:-i or None])):
                    break
            else:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)