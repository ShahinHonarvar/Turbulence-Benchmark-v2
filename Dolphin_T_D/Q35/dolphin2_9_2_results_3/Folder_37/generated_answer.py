def remove_repeat_chars(s):
    found_chars = set()
    for i in range(2, 7):
        if s[i] in s[:i] + s[i + 1:]:
            found_chars.add(s[i])
    return ''.join([ch for ch in s if ch not in found_chars and ch != ''])