def remove_repeat_chars(s):
    unique_chars = set(s[0:6])
    result = [char for char in s if char in unique_chars]
    return ''.join(result)