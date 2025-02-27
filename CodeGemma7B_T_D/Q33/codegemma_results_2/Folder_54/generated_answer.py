def return_vowels(string):
    vowels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowel_range = vowels[23:85]
    vowels_list = []
    for vowel in vowel_range:
        if vowel > vowels[22] and vowel <= vowels[22 + 12]:
            vowels_list.append(vowel)
    return vowels_list or []