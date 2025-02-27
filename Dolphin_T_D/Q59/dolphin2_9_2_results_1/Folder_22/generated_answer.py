import sympy

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[85]
    primes = []
    for i in range(2, x):
        if sympy.isprime(i):
            i_str = str(i)
            while i_str:
                if i_str[0] == '0':
                    break
                if sympy.isprime(int(i_str)):
                    i_str = i_str[1:]
                else:
                    break
            else:
                primes.append(i)
    return sorted(primes)