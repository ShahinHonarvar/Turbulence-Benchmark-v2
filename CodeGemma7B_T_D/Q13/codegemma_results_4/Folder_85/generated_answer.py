from typing import List, Optional

def find_second_largest_num(num_list: List[float]) -> Optional[float]:
    if len(num_list) < 9:
        return None
    sorted_list = sorted(num_list[6:9], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]