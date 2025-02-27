def return_nth_smallest_ascii(a_string):
    a_list = list(a_string)
    a_list_substring = a_list[0:18]
    sorted_list = sorted(a_list_substring, key=ord)
    return sorted_list[17]