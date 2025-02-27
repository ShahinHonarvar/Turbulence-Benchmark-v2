def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[42]
    primes = []
    for i in range(x, 0, -1):
        s = str(i)
        flag = True
        for j in range(len(s) - 1):
            if s[j] == '0':
                flag = False
                break
            if not is_prime(int(s[j:])) or not is_prime(int(s[:j + 1])):
                flag = False
                break
        if flag:
            primes.append(i)
    return sorted(primes)