def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for i in range(641, 872):
        if i < len(s) and s[i] in vowels and ('>' < s[i] <= 'q'):
            result.append(s[i])
    return result