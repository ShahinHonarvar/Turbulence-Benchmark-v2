def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes():
    ltp = set()
    for i in range(1, 10):
        if is_prime(i):
            ltp.add(i)
    for i in range(10, 100):
        if str(i)[0] == '0':
            continue
        if is_prime(i) and i % 100 // 10 in ltp and (i % 100 % 10 in ltp):
            ltp.add(i)
            ltp = ltp | {int(str(x)[1:]) for x in ltp if int(str(x)[1:]) < i}
    return sorted(ltp, reverse=True)

def all_left_truncatable_prime(n):
    x = n[81]
    ltp = left_truncatable_primes()
    return [i for i in ltp if i < x]