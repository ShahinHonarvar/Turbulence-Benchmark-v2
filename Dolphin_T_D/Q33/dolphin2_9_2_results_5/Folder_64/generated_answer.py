def return_vowels(s):
    vowels = []
    for i in range(1, 7):
        if 'F' < s[i] <= 'j' and s[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(s[i])
    return vowels