from typing import List

def return_n_greatest_chars(s: str) -> List[str]:
    return sorted(s, key=ord, reverse=True)[:23]