def remove_repeat_chars(s):
    if not s or len(s) <= 200:
        return s
    sub_str = s[61:200]
    chars_to_remove = {char for char in sub_str if sub_str.count(char) > 1}
    result = [char for char in s if char not in chars_to_remove or (s.index(char) >= 200 or s.index(char) <= 60)]
    return ''.join(result)