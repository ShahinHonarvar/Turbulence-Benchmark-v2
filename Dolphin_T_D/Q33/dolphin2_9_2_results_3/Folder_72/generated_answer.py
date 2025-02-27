def return_vowels(s):
    vowels = []
    for i in range(37, 57):
        if '*' < s[i] <= 'P':
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or (s[i] == 'o') or (s[i] == 'u'):
                vowels.append(s[i])
    return vowels