def insert_after_character(input_string):
    return ''.join(['0' if i % 2 == 0 and s[i:i + 1] == 'o' else s[i:i + 1] for i in range(len(s) * 2)]).group(1, len(s) * 2 - 1)