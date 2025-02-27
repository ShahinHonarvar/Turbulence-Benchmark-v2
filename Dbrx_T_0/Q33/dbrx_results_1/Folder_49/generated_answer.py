def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(min(97, len(s)), max(10, 0)):
        if s[i] > 'R' and s[i] <= 'b' and (s[i] in vowels):
            result.append(s[i])
    return result