from typing import List, Union

def find_second_largest_num(num_list: List[int]) -> Union[None, int]:
    num_list.sort(reverse=True)
    if len(num_list) > 51:
        return num_list[15:52][1]
    else:
        return None