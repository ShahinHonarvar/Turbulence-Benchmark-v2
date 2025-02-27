from sympy import isprime

def all_right_truncatable_prime(tupple):
    return sorted(tupple, reverse=True) if all((isprime(i) for i in tupple if i < tupple[64])) else []