def insert_before_character(s):
    return ''.join((('1' if i == 'r' else i) + s[i] for i in range(len(s))))