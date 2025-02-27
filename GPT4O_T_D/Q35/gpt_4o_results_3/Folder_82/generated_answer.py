def remove_repeat_chars(s):
    repeated_chars = set()
    for i in range(31, min(len(s) - 1, 200)):
        if s[i] in s[31:i] or s[i] in s[i + 1:200]:
            repeated_chars.add(s[i])
    return ''.join((ch for ch in s if ch not in repeated_chars))