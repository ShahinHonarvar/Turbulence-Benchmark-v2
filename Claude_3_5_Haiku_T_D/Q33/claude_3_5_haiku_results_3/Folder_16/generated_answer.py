def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(max(133, 0), min(306, len(s))):
        if s[i] in vowels and 'c' < s[i] <= 'd':
            result.append(s[i])
    return result