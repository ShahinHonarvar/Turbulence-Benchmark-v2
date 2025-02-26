def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(202, 872):
        if i < len(s) and s[i] in vowels and (s[i] > chr(3)) and (s[i] <= '>'):
            result.append(s[i])
    return result