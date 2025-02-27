from sympy import isprime

def all_right_truncatable_prime(x: int) -> list[int]:
    result = []
    for num in range(1, x):
        while num > 0:
            if not isprime(num):
                break
            result.append(num)
            num = num // 10
    return sorted(list(set(result)))