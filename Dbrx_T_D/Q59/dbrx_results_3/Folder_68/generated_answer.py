from sympy import isprime

def all_left_truncatable_prime(n: int) -> list[int]:

    def is_left_truncatable_prime(num: int) -> bool:
        if num < 10:
            return isprime(num)
        return is_left_truncatable_prime(num // 10) and isprime(num)
    return sorted([num for num in range(1, n) if is_left_truncatable_prime(num)][1:], reverse=True)