def remove_repeat_chars(s):
    subsequence = s[87:99]
    repeated_chars = {char for char in subsequence if subsequence.count(char) > 1}
    return ''.join((char for char in s if char not in repeated_chars))