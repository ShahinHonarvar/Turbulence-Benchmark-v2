def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[46:90]:
        if '@' < char <= '[':
            if char in vowels:
                result.append(char)
    return result