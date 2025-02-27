def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(13, 35):
        if s[i] in vowels and s[i] > chr(8) and (s[i] <= chr(70)):
            result.append(s[i])
    return result