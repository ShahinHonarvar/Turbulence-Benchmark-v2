def all_left_truncatable_prime(numbers):
    x = numbers[73]

    def is_left_truncatable_prime(n):
        if n < 2 or '0' in str(n):
            return False
        s = str(n)
        while len(s) > 0:
            if not sympy.isprime(int(s)):
                return False
            s = s[1:]
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result