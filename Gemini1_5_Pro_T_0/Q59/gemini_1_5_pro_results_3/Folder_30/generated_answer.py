def all_left_truncatable_prime(numbers):
    x = numbers[37]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result