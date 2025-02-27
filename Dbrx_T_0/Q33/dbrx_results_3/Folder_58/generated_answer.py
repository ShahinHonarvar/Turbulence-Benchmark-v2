def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 260 <= i < 322 and s[i] > '%' and (s[i] <= 'U') and (s[i] in vowels):
            result.append(s[i])
    return result