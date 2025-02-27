from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[466]
    prime_list = [i for i in range(2, x) if isprime(i)]
    truncatable_list = [i for i in prime_list if all((isprime(int(str(i)[:-j])) for j in range(1, len(str(i)))))]
    return sorted(truncatable_list, reverse=True) if truncatable_list else []