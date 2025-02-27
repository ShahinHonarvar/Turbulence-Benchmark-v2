def return_nth_smallest_ascii(input_string):
    substring = input_string[29:34]
    ordered_substring = sorted(substring, key=lambda x: ord(x))
    if len(ordered_substring) < 5:
        return 'Not enough characters'
    else:
        return ordered_substring[4]