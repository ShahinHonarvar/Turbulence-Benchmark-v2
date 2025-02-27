def insert_before_character(s):
    return ''.join(['H' if s[i - 1:i] == 'C' else s[i - 1:i] for i in range(1, len(s) + 1)])