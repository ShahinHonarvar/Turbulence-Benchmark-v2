def return_nth_smallest_ascii(string):
    chars = [char for char in string[5:11] if char in string]
    return sorted(chars)[5]