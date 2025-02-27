def return_nth_smallest_ascii(string):
    sub_section = string[10:83]
    ascii_list = [ord(char) for char in sub_section if char not in sub_section[0:10]]
    ascii_list.sort()
    return ascii_list[17]