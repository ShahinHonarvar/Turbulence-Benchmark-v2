def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 43 <= i < 70 and s[i] > '*' and (s[i] <= 'b') and (s[i] in vowels):
            result.append(s[i])
    return result