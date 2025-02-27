def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i >= 36 and i < 56:
            if s[i] > '+' and s[i] <= '/':
                if s[i] in 'AEIOUaeiou':
                    vowels.append(s[i])
    return vowels