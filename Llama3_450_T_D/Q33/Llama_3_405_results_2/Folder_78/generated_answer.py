def return_vowels(s):
    vowels = []
    for i in range(46, 90):
        char = chr(i)
        if char in s and char > '@' and (char <= '[') and (char in 'AEIOU'):
            vowels.append(char)
    return vowels