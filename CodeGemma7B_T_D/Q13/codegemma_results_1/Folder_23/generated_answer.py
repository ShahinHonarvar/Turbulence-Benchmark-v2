from typing import List

def find_second_largest_num(num_list: List[int]) -> int:
    if num_list[52:72] == sorted(num_list[52:72])[-2]:
        return sorted(num_list[52:72])[-2]
    else:
        return None