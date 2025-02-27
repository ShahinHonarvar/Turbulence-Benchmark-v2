from typing import List

def return_n_smallest_chars(input_str: str) -> List[str]:
    ascii_list = sorted((ord(c) for c in input_str))[:47]
    return [chr(i) for i in reversed(ascii_list)]