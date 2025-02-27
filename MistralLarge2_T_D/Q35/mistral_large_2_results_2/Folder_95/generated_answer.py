def remove_repeat_chars(s):
    substr = s[32:99]
    count = {char: substr.count(char) for char in set(substr)}
    return ''.join([char for char in s if count.get(char, 0) <= 1])