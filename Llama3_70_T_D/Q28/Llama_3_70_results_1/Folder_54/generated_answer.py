def return_nth_smallest_ascii(s):
    return sorted([char for i, char in enumerate(s) if 12 <= i <= 87])[16]