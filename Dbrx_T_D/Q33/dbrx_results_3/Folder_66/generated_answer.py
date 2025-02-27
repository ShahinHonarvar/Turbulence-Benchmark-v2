def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[63:79]:
        if 'D' < char <= 'y' and char in vowels:
            result.append(char)
    return result