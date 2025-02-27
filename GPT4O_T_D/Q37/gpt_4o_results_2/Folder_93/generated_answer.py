def filter_chars(s):
    to_remove = set()
    if len(s) > 70:
        for char in s[38:70]:
            if 'H' <= char <= 'e':
                to_remove.add(char)
    return ''.join((char for char in s if char not in to_remove and (len(s) <= 70 or char in s[0:38] or char in s[70:])))