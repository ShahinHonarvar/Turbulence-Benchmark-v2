def return_nth_smallest_ascii(str):
    chars = sorted([char for char in str if str.index(char) >= 29 and str.index(char) <= 33])
    return chars[4]