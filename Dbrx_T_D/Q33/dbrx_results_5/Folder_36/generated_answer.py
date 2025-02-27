def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(604, 949):
        if s[i] > 'N' and s[i] <= 'U' and (s[i] in vowels):
            result.append(s[i])
    return result