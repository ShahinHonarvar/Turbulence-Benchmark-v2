def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, 97):
        if i < len(s) and s[i] in vowels and (s[i] > 'R') and (s[i] <= 'b'):
            result.append(s[i])
    return result