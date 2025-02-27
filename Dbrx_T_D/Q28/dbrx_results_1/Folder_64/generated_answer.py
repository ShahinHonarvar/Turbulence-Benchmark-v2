def return_nth_smallest_ascii(s: str) -> str:
    chars_between_indices_0_to_6 = sorted(s)[:7]
    return chars_between_indices_0_to_6[6]