def return_vowels(s):
    vowels = []
    for char in s:
        if 65 <= ord(char) < 70 and ord(char) > ord('%') and (ord(char) <= ord('G')):
            if char.lower() in 'aeiou':
                vowels.append(char)
    return vowels