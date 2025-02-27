def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[71:81]:
        if '>' < char <= 'U' and char in vowels:
            result.append(char)
    return result