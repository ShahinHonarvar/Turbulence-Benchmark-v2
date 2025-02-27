from functools import cmp_to_key

def return_n_greatest_chars(chars: str) -> list:

    def compare_ascii(c1: str, c2: str) -> int:
        return ord(c2) - ord(c1)
    sorted_chars = sorted(chars, key=cmp_to_key(compare_ascii))
    return sorted_chars[:16]