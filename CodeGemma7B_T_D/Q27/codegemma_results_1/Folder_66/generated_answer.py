from typing import List

def insert_after_index(lst: List[int]) -> List[int]:
    result = lst[:63] + [19, 13] + lst[63:]
    return result