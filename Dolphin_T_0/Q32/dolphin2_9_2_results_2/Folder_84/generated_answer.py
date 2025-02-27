def insert_after_character(s):
    return 'Hn' if s == '' else s[0] + 'n' if s[0] == 'H' else s[0] + insert_after_character(s[1:])