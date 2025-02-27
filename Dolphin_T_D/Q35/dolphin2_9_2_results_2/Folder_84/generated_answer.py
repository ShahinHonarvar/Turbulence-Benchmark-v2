def remove_repeat_chars(input_string):
    counts = {}
    for i in range(32, 44):
        if input_string[i] in counts:
            counts[input_string[i]] += 1
        else:
            counts[input_string[i]] = 1
    for char in counts:
        if counts[char] > 1:
            input_string = input_string.replace(char, '')
    return input_string