from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[30]
    truncatable_primes = []
    for i in range(2, x + 1):
        if isprime(i) and '0' not in str(i):
            str_i = str(i)
            for j in range(1, len(str_i)):
                left_trunc = int(str_i[:j])
                right_trunc = int(str_i[j:])
                if isprime(left_trunc) and isprime(right_trunc):
                    truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes