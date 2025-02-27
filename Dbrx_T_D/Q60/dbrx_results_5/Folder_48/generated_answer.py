from sympy import isprime

def all_left_right_truncatable_prime(args):
    lower_limit = min(args)
    upper_limit = max(args)
    primes = [i for i in range(lower_limit, upper_limit + 1) if isprime(i) and '0' not in str(i)]
    truncatable_primes = []
    for prime in primes:
        flag = True
        for i in range(len(str(prime)) - 1):
            if not isprime(int(str(prime)[i:])) or not isprime(int(str(prime)[:-i - 1])):
                flag = False
                break
        if flag:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)