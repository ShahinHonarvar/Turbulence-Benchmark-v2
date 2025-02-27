def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 63 and i < 79:
            if s[i] > 'D' and s[i] <= 'y':
                if s[i] in 'AEIOUaeiou':
                    vowels.append(s[i])
    return vowels