def return_nth_smallest_ascii(s: str) -> str:
    target_indices = s[18:46]
    ascii_list = [ord(char) for char in target_indices]
    ascii_list.sort()
    return chr(ascii_list[6])