from typing import List

def return_n_smallest_chars(input_str: str) -> List[str]:
    sorted_chars = sorted(input_str, key=ord)
    return sorted_chars[-35:][::-1]