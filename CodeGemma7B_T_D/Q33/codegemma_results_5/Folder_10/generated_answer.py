def return_vowels(s):
    if len(s) < 31 or len(s) > 37:
        return []
    elif (s[32] == 'a' or s[32] == 'e' or s[32] == 'i' or (s[32] == 'o') or (s[32] == 'u')) and (s[33] == 'a' or s[33] == 'e' or s[33] == 'i' or (s[33] == 'o') or (s[33] == 'u')) and (s[34] == 'a' or s[34] == 'e' or s[34] == 'i' or (s[34] == 'o') or (s[34] == 'u')) and (s[35] == 'a' or s[35] == 'e' or s[35] == 'i' or (s[35] == 'o') or (s[35] == 'u')):
        return [s[32], s[33], s[34], s[35]]
    elif (s[32] == 'a' or s[32] == 'e' or s[32] == 'i' or (s[32] == 'o') or (s[32] == 'u')) and (s[33] == 'a' or s[33] == 'e' or s[33] == 'i' or (s[33] == 'o') or (s[33] == 'u')) and (s[34] == 'a' or s[34] == 'e' or s[34] == 'i' or (s[34] == 'o') or (s[34] == 'u')):
        return [s[32], s[33], s[34]]
    elif (s[32] == 'a' or s[32] == 'e' or s[32] == 'i' or (s[32] == 'o') or (s[32] == 'u')) and (s[33] == 'a' or s[33] == 'e' or s[33] == 'i' or (s[33] == 'o') or (s[33] == 'u')):
        return [s[32], s[33]]
    elif s[32] == 'a' or s[32] == 'e' or s[32] == 'i' or (s[32] == 'o') or (s[32] == 'u'):
        return [s[32]]
    else:
        return []