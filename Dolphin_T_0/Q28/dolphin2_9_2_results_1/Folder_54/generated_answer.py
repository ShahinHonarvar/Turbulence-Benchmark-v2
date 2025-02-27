def return_nth_smallest_ascii(string):
    char_list = string[12:88]
    ascii_list = [(char, ord(char)) for char in char_list]
    ascii_list.sort(key=lambda x: x[1])
    nth_smallest = ascii_list[16][0]
    return nth_smallest