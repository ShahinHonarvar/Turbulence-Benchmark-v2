from sympy import isprime

def all_left_truncatable_prime(x):
    prime_nums = [i for i in range(2, x) if isprime(i) and str(i).count('0') == 0]
    result = []
    for prime in prime_nums:
        str_prime = str(prime)
        for i in range(1, len(str_prime)):
            if not isprime(int(str_prime[i:])):
                break
        else:
            result.append(prime)
    return sorted(result, reverse=True)