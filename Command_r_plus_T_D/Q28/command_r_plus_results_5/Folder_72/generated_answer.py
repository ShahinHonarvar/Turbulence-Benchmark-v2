def return_nth_smallest_ascii(s: str) -> str:
    subset = [char for char in s[33:61] if 33 <= ord(char) <= 60]
    subset.sort(key=ord)
    return subset[17]