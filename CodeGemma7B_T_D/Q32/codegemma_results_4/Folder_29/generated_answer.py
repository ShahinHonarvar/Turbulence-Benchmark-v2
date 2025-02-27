def insert_after_character(str1):
    return ''.join([ch + 'z' if ch == 'N' else ch for ch in str1])