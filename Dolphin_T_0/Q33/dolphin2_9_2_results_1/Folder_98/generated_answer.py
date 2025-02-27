def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_range = []
    for char in s[3:9]:
        if 's' < char <= 'u' and char in vowels:
            vowels_in_range.append(char)
    return vowels_in_range