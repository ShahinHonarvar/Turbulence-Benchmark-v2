def remove_repeat_chars(s):
    subsequence = s[376:926]
    repeat_chars = {char for char in subsequence if subsequence.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))