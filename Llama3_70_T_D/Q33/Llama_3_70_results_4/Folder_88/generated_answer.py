def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(70, 76):
        if i < len(s) and s[i] > chr(2) and (s[i] <= chr(58)) and (s[i] in vowels):
            result.append(s[i])
    return result