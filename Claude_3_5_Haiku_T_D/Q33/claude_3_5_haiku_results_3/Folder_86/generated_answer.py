def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(s) >= 275:
        for char in s[273:275]:
            if char in vowels and '+' < char <= 'o':
                result.append(char)
    return result