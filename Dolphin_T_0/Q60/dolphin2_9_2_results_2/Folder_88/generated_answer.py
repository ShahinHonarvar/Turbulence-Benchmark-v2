def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[93]
    primes = []
    for i in range(2, x + 1):
        if i == 2 or i == 3 or i == 5 or (i == 7):
            primes.append(i)
        else:
            for c in '234567':
                if c in str(i):
                    break
            else:
                primes.append(i)
    return [i for i in primes if i > int(str(i)[1:-1]) > 0 and is_prime(int(str(i)[1:-1])) and ((i - int(str(i)[1:-1])) % 10 != 5 and (i - int(str(i)[1:-1])) % 2 != 0 and (i - int(str(i)[1:-1]) > 0))]