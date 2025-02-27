def return_n_smallest_chars(s):
    return sorted([char for char in s if ord(char) in sorted([ord(c) for c in s])[:87]], reverse=True)