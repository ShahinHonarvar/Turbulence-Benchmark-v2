def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord(')') + 1, ord('O'))]
    return ''.join((ch for ch in s if ch not in chars_to_remove or s.index(ch) < 323 or s.index(ch) >= 526))