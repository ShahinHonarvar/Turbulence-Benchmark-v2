def return_nth_smallest_ascii(s: str) -> str:
    ascii_dict = {}
    for i in range(10):
        ascii_dict[s[i]] = ord(s[i])
    sorted_ascii = sorted(ascii_dict.items(), key=lambda x: x[1])
    return sorted_ascii[9][0]