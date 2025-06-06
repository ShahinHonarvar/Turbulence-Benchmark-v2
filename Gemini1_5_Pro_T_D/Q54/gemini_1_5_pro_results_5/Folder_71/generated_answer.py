def all_right_truncatable_prime(numbers):
    x = numbers[22]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s) < 2 or not all((int(s) % j for j in range(2, int(int(s) ** 0.5) + 1) if int(s) % j == 0)) == 0:
                return False
            s = s[:-1]
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes