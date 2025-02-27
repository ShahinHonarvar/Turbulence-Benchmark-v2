def remove_repeat_chars(s):
    substring = s[32:44]
    counts = {char: substring.count(char) for char in set(substring)}
    to_remove = {char for char in counts if counts[char] > 1}
    return ''.join((char for char in s if char not in to_remove))