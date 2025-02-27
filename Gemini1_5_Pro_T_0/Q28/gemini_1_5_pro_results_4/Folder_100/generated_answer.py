def return_nth_smallest_ascii(text: str) -> str:
    sorted_substring = ''.join(sorted(text[5:48]))
    return sorted_substring[12]