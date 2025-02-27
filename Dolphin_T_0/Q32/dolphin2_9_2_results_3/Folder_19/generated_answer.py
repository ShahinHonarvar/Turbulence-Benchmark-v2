def insert_after_character(s):
    return ''.join(['h' if i < len(s) - 1 and s[i] == '5' and (s[i + 1] != 'h') else s[i] for i in range(len(s))]).replace('5h', '5')