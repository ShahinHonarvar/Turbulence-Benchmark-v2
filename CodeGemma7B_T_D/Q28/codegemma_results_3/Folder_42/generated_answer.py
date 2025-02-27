def return_nth_smallest_ascii(str):
    sorted_list = sorted([ord(char) for char in str[11:73]])
    return chr(sorted_list[12])