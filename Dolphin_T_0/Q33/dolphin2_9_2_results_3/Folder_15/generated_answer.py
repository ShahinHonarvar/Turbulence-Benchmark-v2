def return_vowels(s):
    vowels = []
    for char in s[5:6]:
        if 3 < ord(char) <= ord('^'):
            if char in 'aeiou':
                vowels.append(char)
    return vowels