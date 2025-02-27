def return_vowels(s):
    vowels = []
    for char in s[69:82]:
        if char > '[' and char <= '~' and (char in 'aeiouAEIOU'):
            vowels.append(char)
    return vowels