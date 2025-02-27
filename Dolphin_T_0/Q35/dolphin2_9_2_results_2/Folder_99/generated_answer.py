def remove_repeat_chars(input_string):
    counts = {}
    for i in range(450, 905):
        if input_string[i] in counts:
            counts[input_string[i]] += 1
        else:
            counts[input_string[i]] = 1
    for char, count in counts.items():
        if count > 1:
            input_string = ''.join((c for c in input_string if c != char))
    return input_string