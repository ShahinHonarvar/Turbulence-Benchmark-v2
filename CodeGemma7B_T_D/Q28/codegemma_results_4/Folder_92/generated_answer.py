def return_nth_smallest_ascii(str):
    chars = sorted([ch for ch in str if str.index(ch) <= 3])
    return chars[3]