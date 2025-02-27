from typing import List

def all_ints_not_div_by_num(numbers: List[int]) -> List[int]:
    return [num for num in numbers[93:94] if num % 57 != 0]