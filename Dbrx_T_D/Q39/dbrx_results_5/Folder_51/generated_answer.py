def return_n_greatest_chars(string):
    sorted_chars = [char for char in string]
    sorted_chars.sort(key=lambda char: ord(char), reverse=True)
    return sorted_chars[:45]