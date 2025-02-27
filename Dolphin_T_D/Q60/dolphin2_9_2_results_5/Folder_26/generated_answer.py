from sympy import isprime

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[81]
    return sorted([i for i in range(2, x + 1) if isprime(i) and (not '0' in str(i)) and all((isprime(int(str(i)[n:-n - 1 if n + 1 < len(str(i)) else len(str(i)) - 1])) for n in range(1, len(str(i)) // 2 + 1)))], reverse=True)