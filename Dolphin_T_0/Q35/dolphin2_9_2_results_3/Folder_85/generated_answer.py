def remove_repeat_chars(string: str) -> str:
    to_remove = [char for char, count in zip(string[1:8], string[1:8].count) if count > 1]
    string = [char for char in string if char not in to_remove]
    return ''.join(string)