def remove_repeat_chars(s):
    substr = s[1:8]
    repeats = set((ch for ch in substr if substr.count(ch) > 1))
    result = ''.join((ch for ch in s if ch not in repeats))
    return result