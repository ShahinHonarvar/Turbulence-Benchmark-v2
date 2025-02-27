def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    if len(numbers) < 21:
        return []
    x = numbers[20]
    truncatable_primes = []
    for i in range(11, x + 1):
        if '0' not in str(i) and is_prime(i) and is_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)