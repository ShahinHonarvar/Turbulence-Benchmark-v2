def return_vowels(s):
    vowels = []
    for i in range(20, 43):
        if 5 < ord(s[i]) <= ord('M') and s[i] in 'AEIOUaeiou':
            vowels.append(s[i])
    return vowels