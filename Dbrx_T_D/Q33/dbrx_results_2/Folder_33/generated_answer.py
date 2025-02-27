def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 163 and i < 771:
            if s[i] > ':' and s[i] <= 'E':
                vowels.append(s[i])
    return vowels