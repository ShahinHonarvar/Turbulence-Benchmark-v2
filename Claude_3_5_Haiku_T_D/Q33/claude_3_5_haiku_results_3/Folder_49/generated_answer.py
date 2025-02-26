def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(10, 97):
        if i < len(s) and s[i] in vowels and ('R' < s[i] <= 'b'):
            result.append(s[i])
    return result