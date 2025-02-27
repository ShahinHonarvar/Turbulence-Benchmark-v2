def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 529 and i < 828:
            if s[i] > 'U' and s[i] <= 'l' and (s[i] in 'AEIOUaeiou'):
                vowels.append(s[i])
    return vowels