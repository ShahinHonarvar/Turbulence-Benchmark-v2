def remove_repeat_chars(input_string):
    chars_to_remove = set()
    for i in range(1, 11):
        if input_string[i] in input_string[:i]:
            chars_to_remove.add(input_string[i])
    altered_string = ''.join((c for c in input_string if c not in chars_to_remove))
    return altered_string