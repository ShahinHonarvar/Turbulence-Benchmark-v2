def return_vowels(s):
    vowels = []
    for char in s[71:81]:
        if '>' < char <= 'U' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels