from sympy import isprime

def all_left_right_truncatable_prime(x):
    return sorted([i for i in range(x, 1, -1) if isprime(i) and str(i).count('0') == 0 and all((isprime(int(str(i)[1:-1])) for i in range(len(str(i)) - 1, 0, -1)))], reverse=True)