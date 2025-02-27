from typing import List

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def is_zero_present(x: int) -> bool:
    return '0' in str(x)

def all_left_truncatable_prime(tup_x: int) -> List[int]:
    x = tup_x[30]
    prime_nums = [i for i in range(x) if is_prime(i) and (not is_zero_present(i))]
    result = []
    for prime in prime_nums:
        temp = prime
        while temp >= 10:
            temp //= 10
            if not is_prime(temp):
                break
        else:
            result.append(prime)
    return sorted(result, reverse=True)