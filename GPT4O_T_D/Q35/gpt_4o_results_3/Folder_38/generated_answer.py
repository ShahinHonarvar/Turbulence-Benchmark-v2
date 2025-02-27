def remove_repeat_chars(s):
    subsequence = s[37:85]
    char_count = {char: subsequence.count(char) for char in set(subsequence)}
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove))
    return result