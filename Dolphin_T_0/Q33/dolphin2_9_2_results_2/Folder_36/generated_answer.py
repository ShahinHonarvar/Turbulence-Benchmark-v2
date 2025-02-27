def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(604, 949):
        if 'n' < s[i] <= 'u' and s[i] in vowels:
            result.append(s[i])
    return result