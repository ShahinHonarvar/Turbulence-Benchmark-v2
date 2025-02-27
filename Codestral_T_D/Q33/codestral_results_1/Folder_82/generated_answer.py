def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(86, 99):
        if i < len(s) and s[i] > 'E' and (s[i] <= 'r') and (s[i].lower() in vowels):
            result.append(s[i])
    return result