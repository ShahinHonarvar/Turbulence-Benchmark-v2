def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(20, 41):
        if s[i] in vowels and s[i] > 'K' and (s[i] <= 'Z'):
            result.append(s[i])
    return result