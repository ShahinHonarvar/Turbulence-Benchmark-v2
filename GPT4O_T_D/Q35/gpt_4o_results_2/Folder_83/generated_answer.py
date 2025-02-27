def remove_repeat_chars(s):
    substring = s[101:200]
    char_count = {char: substring.count(char) for char in set(substring)}
    repeated_chars = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in repeated_chars]
    return ''.join(result)