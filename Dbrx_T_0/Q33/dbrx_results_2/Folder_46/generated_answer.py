def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 10 <= i < 83 and s[i] > '%' and (s[i] <= 'e') and (s[i] in vowels):
            result.append(s[i])
    return result