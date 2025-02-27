def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[8:9]:
        if 'Y' < char <= 's':
            if char in vowels:
                result.append(char)
    return result