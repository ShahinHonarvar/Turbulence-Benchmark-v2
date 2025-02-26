def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(32, 97):
        if i < len(s):
            if s[i] in vowels and 'Q' < s[i] <= ']':
                result.append(s[i])
    return result