def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    output = []
    for char in s[4:8]:
        if 'p' < char <= 'r' and char in vowels:
            output.append(char)
    return output