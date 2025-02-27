def remove_repeat_chars(input_string: str) -> str:
    char_count = {}
    result = ''
    for i in range(len(input_string)):
        if i >= 77 and i < 84:
            if input_string[i] in char_count:
                char_count[input_string[i]] += 1
            else:
                char_count[input_string[i]] = 1
        else:
            result += input_string[i]
    for char, count in char_count.items():
        if count > 1:
            result = result.replace(char, '', count - 1)
    return result