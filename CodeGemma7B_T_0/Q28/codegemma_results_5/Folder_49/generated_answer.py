def return_nth_smallest_ascii(string):
    return sorted([char for char in string[20:81] if char in string])[10]