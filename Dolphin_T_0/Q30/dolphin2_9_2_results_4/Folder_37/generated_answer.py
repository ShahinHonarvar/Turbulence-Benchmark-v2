def insert_before_character(string):
    return ''.join(['a' if i + 1 == j and s[j] == 'U' else s[i] for i, j, s in enumerate(zip(string, string[1:]))]) + string[-1]