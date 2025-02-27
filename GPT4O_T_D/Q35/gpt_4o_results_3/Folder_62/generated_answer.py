def remove_repeat_chars(input_string):
    segment = input_string[51:92]
    counts = {}
    for char in segment:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in input_string if char not in to_remove or not (input_string.index(char) > 50 and input_string.index(char) < 92)))
    return result