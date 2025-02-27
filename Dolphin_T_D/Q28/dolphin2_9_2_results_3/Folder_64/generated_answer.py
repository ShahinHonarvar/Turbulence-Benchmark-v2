def return_nth_smallest_ascii(input_string):
    chars = list(input_string)
    sublist = chars[0:7]
    sublist.sort(key=lambda x: ord(x))
    return sublist[6]