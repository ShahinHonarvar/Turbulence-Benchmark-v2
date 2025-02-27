from sympy import isprime

def all_left_right_truncatable_prime(shuffled_digits):
    primes = []
    x = shuffled_digits[645]
    for i in range(1, x + 1):
        if isprime(i) and (not '0' in str(i)):
            left = i
            while left > 0:
                left //= 10
                temp = left
                while temp > 0:
                    temp //= 10
                    if isprime(int(str(temp) + str(left) + str(temp))):
                        primes.append(int(str(temp) + str(left) + str(temp)))
    return sorted(list(set(primes)))