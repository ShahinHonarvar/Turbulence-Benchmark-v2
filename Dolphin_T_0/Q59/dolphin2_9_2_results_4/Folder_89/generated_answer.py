def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    primeList = []
    for i in reversed(range(x)):
        if i != 0 and is_prime(int(str(i))):
            trunc = i
            while is_prime(trunc):
                trunc = int(''.join(str(trunc)[1:]))
            if trunc == 0:
                primeList.append(i)
    primeList.sort(reverse=True)
    return primeList