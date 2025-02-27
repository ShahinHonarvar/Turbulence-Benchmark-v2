import sympy

def all_left_right_truncatable_prime(numbers):
    x = numbers[177]
    all_prime = [x for x in sympy.primerange(2, x + 1) if all((sympy.isprime(int(str(x)[1:-1])) for l in range(1, len(str(x)) - 1)))]
    all_left_right_truncatable = [x for x in all_prime if all((sympy.isprime(int(str(x)[i:j])) for i in range(len(str(x))) for j in range(i + 1, len(str(x)) + 1)))]
    return all_left_right_truncatable