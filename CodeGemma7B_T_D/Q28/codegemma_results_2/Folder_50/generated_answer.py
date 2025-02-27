def return_nth_smallest_ascii(string):
    return sorted([ch for i, ch in enumerate(string) if 25 <= i <= 88])[10]