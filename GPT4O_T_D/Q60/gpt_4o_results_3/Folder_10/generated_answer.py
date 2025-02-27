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

    def truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 2:
            s = s[1:-1]
            if not is_prime(int(s)):
                return False
        return True
    try:
        x = numbers[38]
    except IndexError:
        return []
    primes = [n for n in range(10, x + 1) if is_prime(n) and truncatable_prime(n)]
    return sorted(primes, reverse=True)