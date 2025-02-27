def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = numbers[97]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i) and is_left_truncatable(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)