def return_n_greatest_chars(string_of_chars):
    sorted_chars = sorted(list(string_of_chars))[-49:]
    sorted_chars[:] = [char for char in sorted_chars if char >= max(sorted_chars) - 48]
    return sorted_chars[::-1]