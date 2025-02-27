def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for char in s[1:4]:
        if 'C' < char <= 'I' and char in vowels:
            result.append(char)
    return result