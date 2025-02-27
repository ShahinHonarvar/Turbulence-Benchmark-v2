def return_nth_smallest_ascii(string):
    return sorted([char for char in string if string.index(char) >= 30 and string.index(char) <= 70])[4]