def return_nth_smallest_ascii(text):
    return min((ch for ch in text if text.index(ch) in range(10)), key=ord)