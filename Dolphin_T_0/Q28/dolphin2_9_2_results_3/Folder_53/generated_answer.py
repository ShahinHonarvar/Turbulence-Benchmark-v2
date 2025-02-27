def return_nth_smallest_ascii(string):
    return sorted([char for i, char in enumerate(string) if 40 <= i <= 60])[18]