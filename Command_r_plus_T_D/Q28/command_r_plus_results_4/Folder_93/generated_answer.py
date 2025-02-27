def return_nth_smallest_ascii(s: str) -> str:
    ascii_dict = {}
    for i, char in enumerate(s[42:60], start=42):
        ascii_dict[char] = ascii_dict.get(char, 0) + 1
    sorted_ascii = sorted(ascii_dict.items(), key=lambda x: (x[1], ord(x[0])))
    nth_smallest = sorted_ascii[16][0]
    return nth_smallest