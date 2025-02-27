def remove_repeat_chars(s):
    if len(s) <= 377:
        return s
    substr = s[376:926]
    to_remove = {char for char in substr if substr.count(char) > 1}
    result = [char for char in s if char not in to_remove or not 377 <= s.index(char) < 926]
    return ''.join(result)