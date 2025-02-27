def all_right_truncatable_prime(numbers):
    x = numbers[429]

    def is_right_truncatable_prime(n):
        if n < 2:
            return False
        s = str(n)
        for i in range(len(s)):
            if int(s[i:]) % 2 == 0 or int(s[i:]) < 2:
                return False
            if not all((int(s[i:]) % j for j in range(3, int(int(s[i:]) ** 0.5) + 1, 2))):
                return False
        return True
    right_truncatable_primes = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes