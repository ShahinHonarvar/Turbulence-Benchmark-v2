def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(2, x + 1):
        s = str(num)
        while len(s) > 1:
            if s[0] == '0' or s[-1] == '0':
                break
            if not is_prime(int(s)):
                break
            s = s[1:-1]
        if len(s) == 1 and is_prime(int(s)):
            primes.append(num)
    primes.sort(reverse=True)
    return primes