def remove_repeat_chars(s):
    target_slice = s[21:51]
    occur_count = {char: target_slice.count(char) for char in set(target_slice) if target_slice.count(char) > 1}
    result = ''.join((c for c in s if c not in occur_count))
    return result