from typing import List

def return_n_smallest_chars(input_str: str) -> List[str]:
    sorted_ascii_values = sorted((ord(c) for c in input_str if input_str.count(c) == 1))[:49]
    return [chr(i) for i in sorted_ascii_values]