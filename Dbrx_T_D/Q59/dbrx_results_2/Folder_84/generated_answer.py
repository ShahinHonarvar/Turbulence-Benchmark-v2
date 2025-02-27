from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    primes = []
    for i in range(2, num_tuple[630]):
        if isprime(i):
            is_left_truncatable = True
            for j in str(i):
                if not isprime(int(str(i)[j:])) or int(j) == 0:
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)