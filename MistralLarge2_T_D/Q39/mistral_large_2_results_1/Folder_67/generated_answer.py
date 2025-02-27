def return_n_greatest_chars(s):
    return sorted([char for char in s if s.count(char) == 1][-66:])