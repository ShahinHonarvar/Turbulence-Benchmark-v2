def all_left_truncatable_prime(numbers):
    x = numbers[175]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10 and is_prime(n):
            return True
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        s = str(n)[1:]
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result