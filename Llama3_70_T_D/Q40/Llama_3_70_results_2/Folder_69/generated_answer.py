def return_n_smallest_chars(s):
    ascii_dict = {}
    for char in s:
        ascii_dict[char] = ord(char)
    sorted_ascii = sorted(ascii_dict.items(), key=lambda x: x[1])
    smallest_65 = [char[0] for char in sorted_ascii[:65]]
    smallest_65.sort(reverse=True)
    return smallest_65