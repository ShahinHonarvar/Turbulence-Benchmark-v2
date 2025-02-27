def remove_repeat_chars(input_string):
    if len(input_string) <= 81:
        return input_string
    substring = input_string[39:81]
    char_counts = {}
    for char in substring:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    to_remove = {char for char, count in char_counts.items() if count > 1}
    result = []
    for char in input_string:
        if char not in to_remove or input_string.index(char) <= 39 or input_string.index(char) >= 81:
            result.append(char)
    return ''.join(result)