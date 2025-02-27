def remove_repeat_chars(s):
    if len(s) <= 40 or len(s) <= 200:
        return s
    sub_str = s[41:200]
    count = {char: sub_str.count(char) for char in set(sub_str)}
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    result = ''
    for char in s:
        if not (41 <= s.index(char) < 200 and char in to_remove):
            result += char
    return result