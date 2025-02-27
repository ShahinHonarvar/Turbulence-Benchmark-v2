def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(641, min(872, len(s))):
        if s[i] in vowels and '>' < s[i] <= 'q':
            result.append(s[i])
    return result