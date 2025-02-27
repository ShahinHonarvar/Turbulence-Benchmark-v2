from typing import List

def sum_in_range(int_list: List[int]) -> int:
    total = 0
    for number in int_list:
        if 739 <= number <= 928:
            total += number
    return total or 0