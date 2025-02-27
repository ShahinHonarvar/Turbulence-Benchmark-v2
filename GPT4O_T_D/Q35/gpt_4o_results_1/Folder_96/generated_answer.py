def remove_repeat_chars(s):
    to_remove = set()
    sub_string = s[61:200]
    for char in set(sub_string):
        if sub_string.count(char) > 1:
            to_remove.add(char)
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 60 or s.index(char) >= 200))
    return result