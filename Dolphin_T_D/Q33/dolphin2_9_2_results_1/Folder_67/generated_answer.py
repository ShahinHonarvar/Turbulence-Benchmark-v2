def return_vowels(s):
    vowels = []
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    for c in s[21:59]:
        if c > '/' and c <= 'a':
            if c in vowels_letters:
                vowels.append(c)
    return vowels