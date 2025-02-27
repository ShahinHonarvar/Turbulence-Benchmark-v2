def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[55]
    right_truncatable_primes = set()
    for i in range(2, x):
        str_i = str(i)
        if all((is_prime(int(str_i[:j + 1])) for j in range(len(str_i)))):
            right_truncatable_primes.add(i)
    return sorted(list(right_truncatable_primes), reverse=True)