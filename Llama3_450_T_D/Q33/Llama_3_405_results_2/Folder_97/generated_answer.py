def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(328, 455):
        if i < len(s) and s[i] > '<' and (s[i] <= 'z') and (s[i] in vowels):
            result.append(s[i])
    return result