def return_nth_smallest_ascii(given_string):
    index = 9
    char_list = []
    while index <= 59:
        char_list.append(given_string[index])
        index += 1
    return sorted(char_list)[5]