def return_vowels(s):
    vowels = []
    for char in s[4:8]:
        if char in 'aeiouAEIOU' and ord(char) > ord('P') and (ord(char) <= ord('r')):
            vowels.append(char)
    return vowels