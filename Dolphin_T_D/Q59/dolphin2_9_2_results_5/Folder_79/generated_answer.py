def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def are_all_primes(s):
        if len(s) == 1:
            return is_prime(int(s))
        for i in range(len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
    x = numbers[91]
    return sorted([int(s) for s in str(x) if are_all_primes(s)])