def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text if text.index(ch) in range(70)])[9]