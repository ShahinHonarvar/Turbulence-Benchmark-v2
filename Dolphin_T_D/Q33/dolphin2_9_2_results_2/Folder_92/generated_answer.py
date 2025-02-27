def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[3:8]:
        if char in vowels and ';' < char <= 'D':
            result.append(char)
    return result