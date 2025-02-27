def remove_repeat_chars(s: str) -> str:
    for char in set(s[100:200]):
        if len(char) > 1:
            raise ValueError('Input string should not contain any substrings of length greater than 1')
        if s[100:200].count(char) > 1:
            s = s.replace(char, '', s[100:200].count(char))
    return s