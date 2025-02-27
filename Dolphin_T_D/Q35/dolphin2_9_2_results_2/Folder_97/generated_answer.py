def remove_repeat_chars(input_string):
    counts = {}
    for i in range(34, 69):
        if input_string[i] not in counts:
            counts[input_string[i]] = 1
        else:
            counts[input_string[i]] += 1
    for key, value in counts.items():
        if value > 1:
            input_string = input_string.replace(key, '')
    return input_string