def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(323, 526):
        if s[i] > '+' and s[i] <= ':' and (s[i] in vowels):
            result.append(s[i])
    return result