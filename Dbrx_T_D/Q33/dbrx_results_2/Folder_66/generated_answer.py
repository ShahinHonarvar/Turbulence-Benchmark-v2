def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = []
    for i in range(63, 79):
        if i < len(s) and s[i] > 'D' and (s[i] <= 'y') and (s[i] in vowels):
            result.append(s[i])
    return result