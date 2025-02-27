def return_vowels(s):
    vowels = []
    vowel_chars = 'aeiou'
    for char in s[641:872]:
        if char > '>' and char <= 'q' and (char in vowel_chars):
            vowels.append(char)
    return vowels