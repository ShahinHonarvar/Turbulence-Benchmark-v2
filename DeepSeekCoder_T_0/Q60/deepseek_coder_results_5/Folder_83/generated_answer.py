def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[24]
    primes = []

    def is_left_right_truncatable(p):
        s = str(p)
        if '0' in s:
            return False
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:len(s) - i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
    return primes