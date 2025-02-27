def return_vowels(s):
    vowels = []
    for char in s[71:88]:
        if 'a' < char <= 'P' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels