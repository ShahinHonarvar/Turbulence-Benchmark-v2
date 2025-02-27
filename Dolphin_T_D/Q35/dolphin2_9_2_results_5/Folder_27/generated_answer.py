def remove_repeat_chars(input_string):
    remove_set = set()
    for i in range(86, 89):
        if input_string.count(input_string[i]) > 1:
            remove_set.add(input_string[i])
    return ''.join([char for char in input_string if char not in remove_set])