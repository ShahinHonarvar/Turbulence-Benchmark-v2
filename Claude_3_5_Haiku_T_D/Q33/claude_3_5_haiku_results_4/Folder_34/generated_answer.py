def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(19, 32):
        if i < len(s) and s[i].lower() in vowels and ('0' < s[i] <= '7'):
            result.append(s[i])
    return result