import sympy

def all_left_truncatable_prime(x):
    prime_list = []
    for num in range(x, 0, -1):
        if sympy.isprime(num):
            trunc = num
            while trunc != 0:
                if not sympy.isprime(trunc):
                    break
                trunc //= 10
            else:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)