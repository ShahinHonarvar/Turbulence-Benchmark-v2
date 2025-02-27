def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def rotate(num):
    return [int(num[i:] + num[:i]) for i in range(len(num) - 1)]

def all_left_right_truncatable_prime(tup):
    x = tup[3]
    primes = [str(i) for i in range(10, x + 1) if is_prime(i)]
    left_right_primes = []
    for p in primes:
        while len(p) > 2:
            p = ''.join(filter(lambda x: x != '0', p))
            if len(p) > 2 and all((is_prime(int(''.join(filter(lambda x: x != p[i] and x != p[-i], p)))) for i in range(len(p) - 1))):
                left_right_primes.append(p)
            else:
                break
        if len(p) == 2 and all((is_prime(int(p[i])) for i in range(len(p)))):
            left_right_primes.append(p)
    return sorted([int(p) for p in left_right_primes], reverse=True)