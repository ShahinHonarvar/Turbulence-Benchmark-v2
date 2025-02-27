def return_n_smallest_chars(s):
    return sorted([char for char in s if char.isprintable()], key=lambda x: ord(x))[-37:][::-1]