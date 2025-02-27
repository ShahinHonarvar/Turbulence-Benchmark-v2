def return_vowels(s):
    vowels = []
    for i in range(17, min(65, len(s))):
        if s[i] > 'U' and s[i] <= '{':
            vowels.append(s[i])
    return vowels