from sympy import isprime

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[54]
    prime_list = [i for i in range(2, x) if isprime(i)]
    trunc_primes = [i for i in prime_list if str(i).count('0') == 0]
    for i in trunc_primes:
        for j in range(len(str(i)) - 1):
            if not isprime(int(str(i)[j:])):
                trunc_primes.remove(i)
    return sorted(trunc_primes)