def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(len(s)):
        if 17 <= i < 65:
            if s[i] > 'U' and s[i] <= '{' and (s[i] in vowels):
                result.append(s[i])
    return result