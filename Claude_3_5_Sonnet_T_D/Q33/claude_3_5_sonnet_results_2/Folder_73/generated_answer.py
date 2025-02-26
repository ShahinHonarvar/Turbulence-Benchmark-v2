def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(47, 89):
        if i < len(s):
            if s[i] in vowels and '@' < s[i] <= 'n':
                result.append(s[i])
    return result