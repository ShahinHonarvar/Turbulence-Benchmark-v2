def return_vowels(s):
    vowels = []
    for char in s[15:86]:
        if ord('@') < ord(char) <= ord('~') and (char in 'aeiou' or char in 'AEIOU'):
            vowels.append(char)
    return vowels