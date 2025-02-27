def remove_repeat_chars(input_str):
    if len(input_str) < 87 or len(input_str) < 16:
        return input_str
    chars_to_remove = set(input_str[16:87:1])
    result = [char for i, char in enumerate(input_str[16:87:1]) if input_str[:16:1] + input_str[87::1]]
    return ''.join(result) + input_str[:16:1] + '' + input_str[87::1]