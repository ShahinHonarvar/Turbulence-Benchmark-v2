def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    N = 'n'
    k = 'k'
    range_vowels = []
    for char in s[23:38]:
        if N < char.lower() <= k and char.lower() in vowels:
            range_vowels.append(char.lower())
    return range_vowels