def all_left_right_truncatable_prime(numbers):
    x = numbers[41]

    def is_prime(n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_left_right_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not (is_prime(int(s[i:])) and is_prime(int(s[:i + 1]))):
                return False
        return True
    result = []
    for num in range(11, x + 1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)