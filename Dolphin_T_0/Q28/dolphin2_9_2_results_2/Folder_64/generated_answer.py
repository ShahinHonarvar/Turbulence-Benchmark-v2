def return_nth_smallest_ascii(s):
    substr = s[:7]
    sorted_substr = ''.join(sorted(list(substr)))
    nth_char = sorted_substr[6]
    return nth_char