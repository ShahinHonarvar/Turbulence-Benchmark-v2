def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 94):
        if i > 4 and s[i] <= 'H' and (s[i] in vowels):
            result.append(s[i])
    return result