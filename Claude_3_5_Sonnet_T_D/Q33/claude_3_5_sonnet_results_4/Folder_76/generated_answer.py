def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(495, 837):
        if i < len(s):
            if s[i] in vowels and 'B' < s[i] <= 't':
                result.append(s[i])
    return result