def return_n_smallest_chars(strng):
    sorted_chars = sorted([char for char in strng], key=lambda x: ord(x))[:47]
    sorted_chars.sort(reverse=True)
    return sorted_chars