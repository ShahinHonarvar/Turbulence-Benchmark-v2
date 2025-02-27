def return_nth_smallest_ascii(text):
    return sorted([c for i, c in enumerate(text) if 18 <= i <= 66])[18]