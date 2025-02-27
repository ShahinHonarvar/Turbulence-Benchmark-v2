def remove_repeat_chars(s):
    chars = set()
    for i in range(4, len(s)):
        if s[i] in s[:4]:
            chars.add(s[i])
    return ''.join([c for c in s if c not in chars])