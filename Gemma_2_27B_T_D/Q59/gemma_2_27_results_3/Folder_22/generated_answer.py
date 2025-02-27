from typing import Tuple

def all_left_truncatable_prime(nums: Tuple[int]) -> list[int]:
    x = nums[85]
    result = []
    for i in range(2, x):
        prime = True
        num_str = str(i)
        if '0' in num_str:
            continue
        for j in range(1, len(num_str)):
            if not is_prime(int(num_str[j:])):
                prime = False
                break
        if prime:
            result.append(i)
    return sorted(result)

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True