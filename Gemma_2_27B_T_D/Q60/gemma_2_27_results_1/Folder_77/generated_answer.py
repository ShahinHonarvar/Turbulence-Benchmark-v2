from typing import List, Tuple

def all_left_right_truncatable_prime(data: Tuple[int]) -> List[int]:
    x = data[767]
    prime_numbers = []
    for num in range(x, 1, -1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            prime_numbers.append(num)
    return sorted(prime_numbers, reverse=True)

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_left_right_truncatable_prime(num: int) -> bool:
    num_str = str(num)
    if '0' in num_str:
        return False
    while len(num_str) > 1:
        num_str = num_str[1:-1]
        if not is_prime(int(num_str)):
            return False
    return True