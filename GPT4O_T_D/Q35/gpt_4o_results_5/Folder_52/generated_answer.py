def remove_repeat_chars(s):
    region = s[39:81]
    char_count = {char: region.count(char) for char in set(region) if region.count(char) > 1}
    result = ''.join((char for char in s if char not in char_count or not 39 <= s.index(char) <= 80))
    return result