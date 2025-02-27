def return_nth_smallest_ascii(char_string):
    indices = list(range(60, 89))
    chars = [char_string[i] for i in indices]
    return sorted(chars)[6]