def filter_chars(in_string):
    chars_to_remove = []
    for i in range(88, 91):
        for j in range(ord('J'), ord('Q') + 1):
            if in_string[i] == chr(j):
                chars_to_remove.append(in_string[i])
    for char in chars_to_remove:
        in_string = in_string.replace(char, '')
    return in_string