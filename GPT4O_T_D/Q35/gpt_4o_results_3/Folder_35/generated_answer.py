def remove_repeat_chars(s):
    subseq = s[78:84]
    repeat_chars = {char for char in subseq if subseq.count(char) > 1}
    return ''.join((char for char in s if char not in repeat_chars))