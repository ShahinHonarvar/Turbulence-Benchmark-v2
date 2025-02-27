def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(min(828, len(s)), max(529, 0)):
        if s[i] in vowels and 'U' < s[i] <= 'l':
            result.append(s[i])
    return result