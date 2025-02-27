def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(13, min(35, len(s))):
        if s[i] in vowels and 8 < ord(s[i]) <= 15:
            result.append(s[i])
    return result