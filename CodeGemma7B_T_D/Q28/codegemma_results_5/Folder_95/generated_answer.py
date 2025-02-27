def return_nth_smallest_ascii(text):
    return sorted([i for i in text[1:47] if i.isalpha()])[12]