def remove_repeat_chars(s):
    substr = s[45:91]
    counts = {char: substr.count(char) for char in set(substr)}
    to_remove = {char for char in counts if counts[char] > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result