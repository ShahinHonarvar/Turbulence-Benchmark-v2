def return_nth_smallest_ascii(string):
    target_chars = sorted([char for char in string if string.index(char) in range(6, 59)])
    return target_chars[18]