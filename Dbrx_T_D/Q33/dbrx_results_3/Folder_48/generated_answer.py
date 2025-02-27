def return_vowels(s):
    range_vowels = []
    for char in s[529:828]:
        if 'U' < char <= 'l' and char in 'aeiouAEIOU':
            range_vowels.append(char)
    return range_vowels