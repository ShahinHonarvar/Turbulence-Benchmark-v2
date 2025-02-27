from typing import List

def sum_ints_div_by_either_nums(int_list: List[int]) -> int:
    result = 0
    for i in range(0, 2):
        if int_list[i] % 6 == 0 or int_list[i] % 4 == 0:
            result += int_list[i]
    return result if result else 0