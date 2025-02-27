def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True)[:7]
    return_list = []
    for char in sorted_chars:
        return_list.append(char)
    return sorted(return_list)