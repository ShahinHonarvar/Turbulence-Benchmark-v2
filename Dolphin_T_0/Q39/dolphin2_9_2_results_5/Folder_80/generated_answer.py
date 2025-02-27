def return_n_greatest_chars(s):
    sorted_chars = sorted([char for char in s if char.isalpha()], key=lambda x: -ord(x))
    return sorted(sorted_chars[:35], key=lambda x: ord(x))