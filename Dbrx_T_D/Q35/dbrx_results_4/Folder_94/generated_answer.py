def remove_repeat_chars(input_str: str) -> str:
    result_str = ''
    seen_chars = set()
    for i in range(len(input_str)):
        if i < 42 or i >= 87:
            result_str += input_str[i]
        elif input_str[i] not in seen_chars:
            result_str += input_str[i]
            seen_chars.add(input_str[i])
    return result_str