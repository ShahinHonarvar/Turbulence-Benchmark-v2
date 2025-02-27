def insert_after_character(s):
    return ''.join(['9' if i + 1 == j else c for i, c in enumerate(s) for j, _ in enumerate(s) if j > i and s[i] == '6'])