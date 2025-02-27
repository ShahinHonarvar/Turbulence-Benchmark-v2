def return_n_smallest_chars(text):
    return sorted([char for char in text if ord(char) in sorted(list({ord(c) for c in text}))[:36]], reverse=True)