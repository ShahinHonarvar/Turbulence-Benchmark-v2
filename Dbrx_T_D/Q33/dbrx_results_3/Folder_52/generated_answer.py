def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(24, 68):
        if i < len(s) and s[i].lower() in vowels and ('f' < s[i].lower() <= '|'):
            result.append(s[i])
    return result