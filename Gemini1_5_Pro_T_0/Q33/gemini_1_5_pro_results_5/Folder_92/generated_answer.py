def return_vowels(s):
    vowels = []
    for i in range(3, 8):
        if i < len(s) and s[i] in 'AEIOUaeiou' and (';' < s[i] <= 'D'):
            vowels.append(s[i])
    return vowels