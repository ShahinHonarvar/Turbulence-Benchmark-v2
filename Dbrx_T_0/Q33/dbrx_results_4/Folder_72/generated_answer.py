def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 37 <= i < 57 and s[i] > '*' and (s[i] <= 'P') and (s[i] in vowels):
            result.append(s[i])
    return result