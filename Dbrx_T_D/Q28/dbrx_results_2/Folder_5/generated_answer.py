def return_nth_smallest_ascii(s: str) -> str:
    relevant_chars = sorted(s[5:90])[12]
    return chr(relevant_chars)