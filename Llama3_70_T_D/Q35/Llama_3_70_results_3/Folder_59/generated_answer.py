def remove_repeat_chars(input_str):
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    repeat_chars = set([char for char in char_count if char_count[char] > 1 and input_str.index(char) > 0 and (input_str.index(char) < 10)])
    result = ''.join([char for char in input_str if char not in repeat_chars])
    return result