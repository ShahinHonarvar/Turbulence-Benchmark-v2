def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(t):
    x = t[792]
    primes = []
    for i in range(x):
        if is_prime(i):
            j = str(i)
            k = len(j)
            flag = True
            while k > 1:
                if not is_prime(int(j[:k])):
                    flag = False
                    break
                k -= 1
            if flag:
                primes.append(i)
    return sorted(primes)