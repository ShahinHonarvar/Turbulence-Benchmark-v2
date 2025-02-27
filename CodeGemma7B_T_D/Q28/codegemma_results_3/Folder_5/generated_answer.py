def return_nth_smallest_ascii(char_str):
    char_str = char_str[5:89]
    return sorted(char_str, key=ord)[12]