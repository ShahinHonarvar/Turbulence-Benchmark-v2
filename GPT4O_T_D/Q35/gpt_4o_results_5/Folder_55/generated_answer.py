def remove_repeat_chars(s):
    substr = s[11:100]
    to_remove = {ch for ch in substr if substr.count(ch) > 1}
    return ''.join((ch for ch in s if ch not in to_remove or not 11 <= s.index(ch) < 100))