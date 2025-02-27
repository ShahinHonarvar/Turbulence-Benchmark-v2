def palindromes_between_indices(s):
    s = ''.join((c for c in s.lower() if c.isalpha()))
    substring = s[3:5]
    if substring == substring[::-1]:
        return {substring}
    elif substring[0] == substring[2]:
        return {substring}
    elif substring[0] == substring[4] or substring[1] == substring[3]:
        return {substring}
    else:
        return set()