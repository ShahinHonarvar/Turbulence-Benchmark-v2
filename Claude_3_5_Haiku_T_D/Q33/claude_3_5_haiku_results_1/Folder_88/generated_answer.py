def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(70, 76):
        if i < len(s) and s[i] in vowels and (ord('2') < ord(s[i]) <= ord(':')):
            result.append(s[i])
    return result