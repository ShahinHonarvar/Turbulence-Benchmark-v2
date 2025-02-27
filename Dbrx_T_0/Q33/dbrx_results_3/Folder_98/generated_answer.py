def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[3:9]:
        if 's' < char <= 'u' and char in vowels:
            result.append(char)
    return result