def return_n_greatest_chars(s):
    num_chars = 34
    sorted_chars = sorted([char for char in s if char.isalpha()], key=lambda x: -ord(x))
    return sorted_chars[:num_chars]