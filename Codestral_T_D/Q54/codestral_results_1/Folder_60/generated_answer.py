def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[87]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            is_right_truncatable = all((is_prime(int(num_str[:j])) for j in range(1, len(num_str))))
            if is_right_truncatable:
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)