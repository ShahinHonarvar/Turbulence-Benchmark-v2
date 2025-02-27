def return_nth_smallest_ascii(s: str) -> str:
    ascii_values = [ord(c) for c in s if 3 <= s.index(c) <= 52]
    sorted_ascii_values = sorted(set(ascii_values))
    return chr(sorted_ascii_values[7]) if len(sorted_ascii_values) > 7 else ''