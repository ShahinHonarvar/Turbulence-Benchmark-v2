def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(56, 90):
        if s[i].lower() > 'k' and s[i].lower() <= 'z' and (s[i].lower() in vowels):
            result.append(s[i])
    return result