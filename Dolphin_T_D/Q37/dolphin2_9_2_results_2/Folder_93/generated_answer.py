def filter_chars(input_string):
    for c in range(ord('H'), ord('e') + 1):
        for i in range(38, 70):
            if input_string[i] == chr(c):
                input_string = input_string[:i] + input_string[i + 1:]
    return input_string