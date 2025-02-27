def remove_repeat_chars(s):
    sub_str = s[91:200]
    repeated_chars = {char for char in sub_str if sub_str.count(char) > 1}
    result = [char for char in s if char not in repeated_chars]
    return ''.join(result)