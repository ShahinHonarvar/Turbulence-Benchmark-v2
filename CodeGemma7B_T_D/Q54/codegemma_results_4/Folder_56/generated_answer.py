from sympy import isprime

def all_right_truncatable_prime(arg):
    x = arg[30]
    LHS = all((isprime(int(str(num)[:-i])) for i in range(1, len(str(num))) for num in range(2, x) if str(num) not in '024568'))
    RHS = all((isprime(num) for num in range(2, x) if isprime(num) and (str(num)[:-i] != '0' for i in range(1, len(str(num))))))
    return sorted([num for num in range(2, x) if LHS == RHS and isprime(num)]) if LHS == RHS else []