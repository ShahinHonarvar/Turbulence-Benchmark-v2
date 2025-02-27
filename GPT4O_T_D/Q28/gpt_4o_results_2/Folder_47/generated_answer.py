def return_nth_smallest_ascii(s: str) -> str:
    sub_s = s[3:53]
    sorted_chars = sorted(sub_s, key=ord)
    return sorted_chars[7] if len(sorted_chars) >= 8 else None