def return_nth_smallest_ascii(text):
    return sorted([ord(text[i]) for i in range(34, min(85, len(text)))])[19] if len(text) > 34 else -1