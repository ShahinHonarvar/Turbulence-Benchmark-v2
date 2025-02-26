def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(40, 91):
        if i < len(s):
            if s[i] in vowels and 'A' < s[i] <= 'x':
                result.append(s[i])
    return result