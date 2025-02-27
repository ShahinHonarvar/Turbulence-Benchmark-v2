def return_vowels(s):
    vowels = []
    for i in range(3, 9):
        if i < len(s) and 'S' < s[i] <= 'U' and (s[i] in 'AEIOUaeiou'):
            vowels.append(s[i])
    return vowels