def return_n_smallest_chars(s):
    return sorted([char for char in s if len(s) >= 64], key=lambda x: ord(x))[-64:][::-1]