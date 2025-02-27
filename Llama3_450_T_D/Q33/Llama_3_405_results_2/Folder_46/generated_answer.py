def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(10, 83):
        if i < len(s) and s[i] in vowels and ('%' < s[i] <= 'e'):
            result.append(s[i])
    return result