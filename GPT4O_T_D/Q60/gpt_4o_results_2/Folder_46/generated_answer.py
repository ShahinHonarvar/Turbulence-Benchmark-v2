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

    def left_right_truncatable(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    x = numbers[33]
    truncatable_primes = []
    for i in range(10, x + 1):
        if '0' not in str(i) and left_right_truncatable(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)