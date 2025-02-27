def remove_repeat_chars(s):
    start, end = (70, 97)
    substr = s[start + 1:end]
    repeat_chars = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars or not start < s.index(char) < end))