def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True

def all_left_right_truncatable_prime(t):
    x = t[760]
    primes = []
    for i in range(2, x + 1):
        if '0' not in str(i) and is_prime(i):
            temp = i
            strip_num = str(temp)
            while len(strip_num) > 1:
                if not is_prime(int(strip_num)):
                    break
                strip_num = strip_num[1:-1]
            else:
                primes.append(temp)
    primes.sort(reverse=True)
    return primes