def return_vowels(txt):
    vowels = []
    for i, char in enumerate(txt):
        if i >= 43 and i < 70:
            if char in ['a', 'e', 'i', 'o', 'u'] and ord(char) > ord('*') and (ord(char) <= ord('b')):
                vowels.append(char)
    return vowels