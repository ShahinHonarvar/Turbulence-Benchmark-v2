def remove_repeat_chars(str):
    result = [char for idx, char in enumerate(str) if idx not in range(44, 78) or str.index(char) == idx]
    return ''.join(result)