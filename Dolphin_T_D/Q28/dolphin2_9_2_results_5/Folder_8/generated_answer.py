def return_nth_smallest_ascii(string):
    sub_string = string[60:89]
    list_of_chars = list(set(sub_string))
    list_of_chars.sort(key=lambda x: x.encode('utf-8'))
    return list_of_chars[6]