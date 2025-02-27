def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(19, 32):
        if 0 < ord(s[i]) <= 7:
            if s[i] in vowels:
                result.append(s[i])
    return result