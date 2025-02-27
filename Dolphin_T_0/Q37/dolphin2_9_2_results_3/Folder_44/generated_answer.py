def filter_chars(string):
    chars_to_remove = [string[i] for i in range(21, 44) if string[i] >= '+' and string[i] <= '8']
    result = ''.join([char for char in string if char not in chars_to_remove])
    return result