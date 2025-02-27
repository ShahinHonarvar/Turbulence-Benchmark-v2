from typing import List

def find_second_largest_num(num_list: List[int]) -> int or None:
    if 25 <= len(num_list) <= 200:
        num_list.sort(reverse=True)
        for index in range(14, 65):
            if index in range(len(num_list)):
                return num_list[index]
    return None