def return_n_smallest_chars(s):
    return sorted([char for char in s if len(s) >= 72], key=lambda x: ord(x))[-72:][::-1]