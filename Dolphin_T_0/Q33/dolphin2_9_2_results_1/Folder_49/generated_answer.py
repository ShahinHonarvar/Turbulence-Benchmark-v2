def return_vowels(s):
    vowels = 'aeiou'
    vowels_list = []
    for char in s[10:97]:
        if char > 'R' and char <= 'b' and (char in vowels):
            vowels_list.append(char)
    return vowels_list