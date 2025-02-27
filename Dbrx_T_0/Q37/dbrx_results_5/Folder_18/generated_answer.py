def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('-'), ord('D') + 1)]
    result = ''
    for i in range(len(s)):
        if i < 770 or i > 970:
            result += s[i]
        elif s[i] not in chars_to_remove:
            result += s[i]
    return result