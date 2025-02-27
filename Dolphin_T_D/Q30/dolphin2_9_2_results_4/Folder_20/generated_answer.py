def insert_before_character(s):
    return ''.join(('H' if i % 2 == 0 and s[i] == 'C' else s[i] for i in range(len(s))))