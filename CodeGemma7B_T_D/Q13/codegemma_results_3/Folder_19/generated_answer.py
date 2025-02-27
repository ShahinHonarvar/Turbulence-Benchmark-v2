from typing import List

def find_second_largest_num(num_list: List[int]) -> int:
    if len(num_list) > 3:
        sorted_list = sorted(num_list)
        return sorted_list[-4]
    else:
        return None