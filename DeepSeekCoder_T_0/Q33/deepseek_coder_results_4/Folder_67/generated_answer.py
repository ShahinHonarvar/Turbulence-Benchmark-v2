def return_vowels(s):
    vowels = []
    for char in s[21:59]:
        if char > '/' and char <= 'a' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels