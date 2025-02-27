def return_vowels(s):
    vowels = []
    for ch in s[40:94]:
        if 'A' <= ch.upper() <= 'H':
            vowels.append(ch)
    return vowels