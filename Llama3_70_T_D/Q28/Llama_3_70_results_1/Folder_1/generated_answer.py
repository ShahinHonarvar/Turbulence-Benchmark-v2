def return_nth_smallest_ascii(s):
    return sorted([char for i, char in enumerate(s) if 21 <= i <= 59])[10]