from sympy import isprime

def all_left_truncatable_prime(t):
    return sorted([i for i in t[:433] if isprime(int(str(i)[:-j])) and '0' not in str(i) for j in range(1, len(str(i))) and isprime(int(str(i)[:-j]))], reverse=True)