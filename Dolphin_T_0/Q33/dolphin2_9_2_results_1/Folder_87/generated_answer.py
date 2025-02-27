def return_vowels(s):
    vowels = 'aeiou'
    returned_vowels = []
    for char in s[34:58]:
        if char > 'b' and char <= 'o' and (char in vowels):
            returned_vowels.append(char)
    return returned_vowels