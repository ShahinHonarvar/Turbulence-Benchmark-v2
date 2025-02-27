def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        num_str = str(n)
        for i in range(len(num_str) - 1, 0, -1):
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = numbers[433]
    primes = []
    for i in range(x - 1, 1, -1):
        if is_right_truncatable_prime(i):
            primes.append(i)
    return sorted(primes, reverse=True)