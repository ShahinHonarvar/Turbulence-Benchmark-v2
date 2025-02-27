def remove_repeat_chars(input_str):
    processed_str = ''
    unique_chars = set()
    for i in range(len(input_str)):
        if i < 450 or i >= 905 or input_str[i] not in unique_chars:
            processed_str += input_str[i]
            if i >= 450 and i < 905:
                unique_chars.add(input_str[i])
    return processed_str