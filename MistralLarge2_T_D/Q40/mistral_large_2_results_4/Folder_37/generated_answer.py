def return_n_smallest_chars(s):
    return sorted([char for char in s if char.isalpha()], key=ord, reverse=True)[:26]