def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(32, 97):
        if i < len(s) and s[i] in vowels and ('Q' < s[i] <= ']'):
            result.append(s[i])
    return result