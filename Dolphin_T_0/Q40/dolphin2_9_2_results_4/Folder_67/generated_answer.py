def return_n_smallest_chars(input_str):
    char_set = set(input_str)
    if len(char_set) < 66:
        return 'Not enough distinct characters in the string'
    else:
        sorted_chars = sorted(char_set, key=lambda x: ord(x))
        return sorted_chars[:66]