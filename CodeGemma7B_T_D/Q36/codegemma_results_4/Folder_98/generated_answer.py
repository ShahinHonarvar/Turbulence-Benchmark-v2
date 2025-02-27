def filter_chars(s):
    return ''.join([ch for ch in s if ord(ch) <= ord('1') or ord(ch) >= ord('J') or ch == s[4:8][i] or (not s[4:8][i].isalnum()) or (i not in [4, 5, 6] and ch.isalnum())])