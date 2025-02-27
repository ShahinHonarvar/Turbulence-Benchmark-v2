def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[41:50]:
        if 'W' < char <= '[':
            if char in vowels:
                result.append(char)
    return result