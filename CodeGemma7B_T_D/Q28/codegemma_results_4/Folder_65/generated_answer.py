def return_nth_smallest_ascii(text):
    return min([ch for i, ch in enumerate(text, start=1) if 32 <= i <= 67], key=ord)