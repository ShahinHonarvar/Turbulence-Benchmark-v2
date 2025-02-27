from sympy import isprime

def all_left_right_truncatable_prime(upper_bound: tuple) -> list:
    if len(upper_bound) < 175:
        return []
    x = upper_bound[175]
    ltrunc_prime = []
    rtrunc_prime = []

    def is_left_and_right_truncatable_prime(n: int) -> bool:
        if n < 10:
            return isprime(n)
        if n % 10 == 0 or n < 10:
            return False
        if not isprime(n):
            return False
        digits = list(str(n))
        return all((isprime(int(digits[i:])) and isprime(int(''.join(digits[:i + 1]))) for i in range(len(digits))))
    for i in range(1, 10):
        if isprime(i):
            ltrunc_prime.append(i)
            rtrunc_prime.append(i)
    for i in range(10, x + 1):
        if is_left_and_right_truncatable_prime(i):
            ltrunc_prime.append(i)
            rtrunc_prime.append(i)
    return sorted(list(set(ltrunc_prime) & set(rtrunc_prime)))