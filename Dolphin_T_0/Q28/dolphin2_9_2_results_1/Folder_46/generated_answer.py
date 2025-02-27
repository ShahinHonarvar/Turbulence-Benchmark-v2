def return_nth_smallest_ascii(string):
    sub_string = string[34:86]
    sorted_characters = sorted(set(sub_string), key=ord)
    return sorted_characters[19]