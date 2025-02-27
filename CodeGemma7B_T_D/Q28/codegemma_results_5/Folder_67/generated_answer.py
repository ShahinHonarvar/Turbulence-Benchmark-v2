def return_nth_smallest_ascii(word):
    first_range = sorted(word[60:84])
    second_range = sorted(word[84:])
    return first_range[13] + second_range[0]