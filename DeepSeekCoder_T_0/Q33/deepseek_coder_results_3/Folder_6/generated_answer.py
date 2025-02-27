def return_vowels(s):
    vowels = []
    for char in s[20:34]:
        if 'U' < char <= 'i' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels