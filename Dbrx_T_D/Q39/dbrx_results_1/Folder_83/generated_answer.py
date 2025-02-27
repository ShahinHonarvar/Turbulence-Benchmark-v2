def return_n_greatest_chars(string_of_chars: str) -> list:
    ascii_list = []
    for char in string_of_chars:
        ascii_list.append(ord(char))
    ascii_list = sorted(ascii_list)
    n_greatest = []
    for i in range(37, -1, -1):
        for char in string_of_chars:
            if ord(char) == ascii_list[i]:
                n_greatest.append(char)
                break
    return n_greatest