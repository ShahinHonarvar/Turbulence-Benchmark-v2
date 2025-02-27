def all_left_truncatable_prime(numbers):
    x = numbers[77]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10 or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:]
            if not is_prime(int(s)):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_prime(i) and is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result