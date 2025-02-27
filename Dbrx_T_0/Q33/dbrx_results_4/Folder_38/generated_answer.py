def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(len(s)):
        if s[i] >= 'U' and s[i] <= '{' and (i >= 17) and (i < 65):
            if s[i] in vowels:
                result.append(s[i])
    return result