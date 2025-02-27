def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[81]
    right_truncatable_primes = []
    for i in range(2, x):
        str_i = str(i)
        while str_i and is_prime(int(str_i)):
            str_i = str_i[:-1]
        if not str_i:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)