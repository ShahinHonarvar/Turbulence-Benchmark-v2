def return_vowels(s):
    vowels = []
    for char in s[65:70]:
        if char > '%' and char <= 'G':
            vowels.append(char)
    return vowels