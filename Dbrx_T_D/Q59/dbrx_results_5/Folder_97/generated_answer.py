def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes():
    for i in range(10, 1, -1):
        if not is_prime(i):
            continue
        result = []
        for j in range(1, 10):
            if j % i == 0:
                continue
            num = j * 10 + i
            if is_prime(num):
                result.append(num)
        if result:
            yield result

def all_left_truncatable_prime(t):
    x = t[645]
    ltp = list(left_truncatable_primes())
    result = []
    for i in ltp:
        if len(i) >= len(str(x)):
            break
        result.extend((j for j in i if j < x))
    return sorted(result)