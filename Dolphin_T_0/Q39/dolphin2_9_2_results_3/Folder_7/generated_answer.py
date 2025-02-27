def return_n_greatest_chars(s):
    sorted_chars = sorted([char for char in s if char.isalpha()], reverse=True)[:49]
    return sorted(sorted_chars)