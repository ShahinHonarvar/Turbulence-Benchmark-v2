def return_nth_smallest_ascii(string):
    sub_string = string[25:46]
    listified_substring = list(sub_string)
    ascii_values = [ord(i) for i in listified_substring]
    ascii_values.sort()
    return listified_substring[ascii_values.index(ascii_values[10])]