def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for char in s[46:90]:
        if char > '@' and char <= '[':
            if char in vowels:
                result.append(char)
    return result