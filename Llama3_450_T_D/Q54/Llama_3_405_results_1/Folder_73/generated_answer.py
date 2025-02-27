def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    right_truncatable_primes = []
    for num in range(2, x):
        str_num = str(num)
        while len(str_num) > 0 and is_prime(int(str_num)):
            str_num = str_num[:-1]
        if len(str_num) == 0:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)