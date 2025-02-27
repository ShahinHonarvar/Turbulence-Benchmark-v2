from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[78]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and isprime(num):
            i, j = (len(str(num)) - 1, 1)
            while i > j:
                i -= 1
                j += 1
                if not isprime(int(str(num)[j:i])):
                    break
            else:
                primes.append(num)
    return sorted(primes, reverse=True)