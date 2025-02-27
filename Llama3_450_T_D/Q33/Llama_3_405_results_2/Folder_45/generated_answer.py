def return_vowels(s):
    vowel_set = set('aeiouAEIOU')
    result = []
    for i in range(43, min(70, len(s))):
        if s[i] in vowel_set and '*' < s[i] <= 'b':
            result.append(s[i])
    return result