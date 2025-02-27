def return_nth_smallest_ascii(s):
    return sorted([char for i, char in enumerate(s) if 25 <= i <= 88])[10]