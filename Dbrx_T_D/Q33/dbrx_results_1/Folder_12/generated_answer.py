def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] > 'Z' and s[i] <= '}' and (s[i] in vowels) and (13 <= i < 37):
            result.append(s[i])
    return result