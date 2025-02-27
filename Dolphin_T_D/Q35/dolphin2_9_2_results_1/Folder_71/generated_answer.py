def remove_repeat_chars(s):
    count = {}
    chars_to_remove = set()
    for i in range(20, 35):
        if s[i] not in count:
            count[s[i]] = 1
        else:
            count[s[i]] += 1
            if count[s[i]] > 1:
                chars_to_remove.add(s[i])
    output = ''
    for char in s:
        if char not in chars_to_remove:
            output += char
    return output