def remove_repeat_chars(s):
    subsequence = s[39:52]
    repeat_chars = {char for char in subsequence if subsequence.count(char) > 1}
    result = ''.join((char for char in s if char not in repeat_chars or s.index(char) < 39 or s.index(char) >= 52))
    return result