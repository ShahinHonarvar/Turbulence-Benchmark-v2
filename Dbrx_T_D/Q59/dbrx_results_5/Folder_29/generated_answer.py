from sympy import isprime

def all_left_truncatable_prime(n_tuple):
    primes = []
    for num in range(1, n_tuple[54]):
        if str(num)[0] == '0':
            continue
        prime = int(str(num))
        while len(str(prime)) > 0:
            if not isprime(prime):
                break
            primes.append(prime)
            prime = int(str(prime)[1:])
    return sorted(list(set(primes)), reverse=True)