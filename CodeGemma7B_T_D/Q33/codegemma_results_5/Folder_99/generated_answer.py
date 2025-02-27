def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for v in vowels:
        if str[vowels.index(v) + 323] == '+' and str[vowels.index(v) + 526] == ':':
            vowel_count += 1
    return vowel_count