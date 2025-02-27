def remove_repeat_chars(s):
    chars_removed = []
    for i in range(len(s)):
        if i < 16 or i >= 87:
            if s[i] not in chars_removed:
                chars_removed.append(s[i])
        elif s[i] not in s[16:87]:
            if s[i] not in chars_removed:
                chars_removed.append(s[i])
    return ''.join(chars_removed)