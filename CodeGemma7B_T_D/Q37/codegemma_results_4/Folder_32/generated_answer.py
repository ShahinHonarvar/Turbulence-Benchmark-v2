def filter_chars(str):
    return ''.join([ch for ch in str if (ch >= 'w' and ch <= '{') and 23 <= str.index(ch) <= 89])