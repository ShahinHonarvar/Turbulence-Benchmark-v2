def return_nth_smallest_ascii(text):
    return sorted([char for char in text if text.index(char) in range(33, 86)])[12]