def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 29 and i < 73:
            if s[i] > '#' and s[i] <= '(':
                if s[i] in 'aeiouAEIOU':
                    vowels.append(s[i])
    return vowels