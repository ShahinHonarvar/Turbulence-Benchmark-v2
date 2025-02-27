def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if 45 <= i < 76 and 'b' < s[i] <= 'z' and (s[i] in vowels):
            result.append(s[i])
    return result