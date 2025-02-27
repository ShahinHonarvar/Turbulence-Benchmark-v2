from sympy import isprime

def all_right_truncatable_prime(args):
    x = args[14]
    result = sorted([num for num in range(x - 1, 0, -1) if all((isprime(num // int(str(num)[-i])) for i in range(1, len(str(num)))))], reverse=True)
    return result if result else []