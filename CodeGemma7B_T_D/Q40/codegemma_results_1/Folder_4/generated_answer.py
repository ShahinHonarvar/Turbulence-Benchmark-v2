def return_n_smallest_chars(given_str):
    n = 0
    ascii_list = []
    output_list = []
    for c in given_str:
        ascii_list.append(ord(c))
    ascii_list.sort()
    while n != 90:
        output_list.append(chr(ascii_list.pop()))
        n += 1
    return output_list[::-1]