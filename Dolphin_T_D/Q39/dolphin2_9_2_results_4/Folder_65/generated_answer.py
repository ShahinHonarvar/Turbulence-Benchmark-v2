def return_n_greatest_chars(string):
    distinct_chars_list = list(set(string))
    sorted_chars_list = sorted(distinct_chars_list, key=lambda x: ord(x))
    reversed_list = sorted_chars_list[::-1]
    n_greatest_chars = reversed_list[:27]
    return n_greatest_chars