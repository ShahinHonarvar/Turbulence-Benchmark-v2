def remove_repeat_chars(s):
    sub_seq = s[410:502]
    to_remove = {char for char in sub_seq if sub_seq.count(char) > 1}
    return ''.join((char for char in s if char not in to_remove or s[410:502].count(char) == 1))