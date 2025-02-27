def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 86:
        return []

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

    def left_right_truncate(n):
        s = str(n)
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i + 1])):
                return False
        return True
    x = numbers[86]
    result = [n for n in range(11, x + 1) if is_prime(n) and left_right_truncate(n)]
    return sorted(result, reverse=True)