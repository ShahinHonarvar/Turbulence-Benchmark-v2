from sympy import isprime

def all_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x):
        if isprime(i):
            trunc = i
            while trunc > 0:
                if not isprime(trunc):
                    break
                trunc //= 10
            else:
                prime_numbers.append(i)
    return sorted(prime_numbers, reverse=True)