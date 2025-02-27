def return_vowels(s):
    vowels = []
    for i in range(170, 645):
        try:
            if 'E' < s[i] <= '~' and s[i] in 'AEIOUaeiou':
                vowels.append(s[i])
        except IndexError:
            break
    return vowels