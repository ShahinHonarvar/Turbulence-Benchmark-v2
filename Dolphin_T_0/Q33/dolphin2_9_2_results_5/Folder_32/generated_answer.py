def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(45, 76):
        char = s[i]
        if 'b' < char <= 'z' and char in vowels:
            result.append(char)
    return result