def return_nth_smallest_ascii(text):
    return sorted([char for char in text[50:76] if char in text])[6]