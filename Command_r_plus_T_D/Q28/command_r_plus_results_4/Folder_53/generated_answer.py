def return_nth_smallest_ascii(s: str) -> str:
    ascii_dict = {}
    for i, char in enumerate(s[40:61], start=40):
        ascii_dict[char] = ascii_dict.get(char, 0) + 1
    sorted_ascii = sorted(ascii_dict.items(), key=lambda x: x[1])
    nth_smallest = sorted_ascii[18][0]
    return nth_smallest