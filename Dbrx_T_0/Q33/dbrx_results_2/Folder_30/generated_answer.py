def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(len(s)):
        if 11 <= i < 61 and 'M' < s[i] <= 'W' and (s[i] in vowels):
            result.append(s[i])
    return result