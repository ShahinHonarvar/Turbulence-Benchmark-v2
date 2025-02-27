def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in s[56:68]:
        if 'M' < char <= 'X' and char.upper() in vowels:
            result.append(char)
    return result