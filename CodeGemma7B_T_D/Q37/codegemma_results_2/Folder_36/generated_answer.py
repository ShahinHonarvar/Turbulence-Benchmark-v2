def filter_chars(string):
    return ''.join([ch for ch in string if (ord(ch) > ord(',') and ord(ch) <= ord('3')) and (ord(ch) < ord('A') or ord(ch) >= ord('a') or ord(ch) == ord(' '))])