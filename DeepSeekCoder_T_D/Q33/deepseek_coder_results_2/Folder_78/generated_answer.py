def return_vowels(s):
    vowels = []
    for char in s[46:90]:
        if '@' < char <= '[':
            if char in 'AEIOUaeiou':
                vowels.append(char)
    return vowels