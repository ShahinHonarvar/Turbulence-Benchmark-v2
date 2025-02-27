def remove_repeat_chars(original_string):
    tally = {}
    new_string = ''
    for index in range(4):
        if original_string[index] not in tally:
            new_string += original_string[index]
            tally[original_string[index]] = 1
    return new_string