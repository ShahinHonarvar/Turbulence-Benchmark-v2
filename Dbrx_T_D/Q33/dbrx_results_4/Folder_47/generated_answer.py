def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 23 <= i < 38 and 'N' < s[i] <= 'k' and (s[i] in vowels):
            result.append(s[i])
    return result