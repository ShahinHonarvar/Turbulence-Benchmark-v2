def is_prime(n):
    if n in (0, 1):
        return False
    elif n in (2, 3):
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(inputs):
    x = inputs[97]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i):
            t = i
            while t > 1:
                t = int(str(t)[-1])
                if not is_prime(t):
                    break
            else:
                primes.append(i)
    return primes[::-1]