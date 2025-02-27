def remove_repeat_chars(s):
    between_90_97 = ''.join(sorted(set(s[90:97]), key=s[90:97].index))
    to_remove = [char for char in between_90_97 if s[90:97].count(char) > 1]
    return ''.join([char for char in s if char not in to_remove])