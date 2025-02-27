from typing import List

def return_n_greatest_chars(string: str) -> List[str]:
    chars = list(string)
    chars.sort(key=lambda char: ord(char), reverse=True)
    return chars[:38]