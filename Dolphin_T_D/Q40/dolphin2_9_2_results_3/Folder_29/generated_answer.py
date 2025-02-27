def return_n_smallest_chars(string):
    char_list = list(string)
    char_list.sort()
    sorted_list = char_list[:23]
    sorted_list.sort(reverse=True)
    return sorted_list