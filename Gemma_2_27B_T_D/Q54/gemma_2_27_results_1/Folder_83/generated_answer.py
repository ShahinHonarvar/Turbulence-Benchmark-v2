def all_right_truncatable_prime(numbers):
    x = numbers[24]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        s = str(i)
        is_right_truncatable = True
        for j in range(len(s)):
            if not is_prime(int(s[j:])):
                is_right_truncatable = False
                break
        if is_right_truncatable:
            right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes)