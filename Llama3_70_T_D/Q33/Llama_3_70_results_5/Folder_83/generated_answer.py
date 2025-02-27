def return_vowels(s):
    vowels = []
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            if char in 'aeiou' and ord(char) > ord('_') and (ord(char) <= ord('x')):
                vowels.append(char)
    return vowels