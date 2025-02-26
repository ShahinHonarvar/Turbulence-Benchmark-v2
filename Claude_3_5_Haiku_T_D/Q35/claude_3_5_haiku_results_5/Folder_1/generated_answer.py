def remove_repeat_chars(s):
    if len(s) <= 18:
        return s
    substr = s[18:88]
    chars_to_remove = set()
    for i in range(len(substr)):
        if substr.count(substr[i]) > 1 and substr[i] not in chars_to_remove:
            chars_to_remove.add(substr[i])
    result = s[:18] + ''.join((char for char in substr if char not in chars_to_remove)) + s[88:]
    return result