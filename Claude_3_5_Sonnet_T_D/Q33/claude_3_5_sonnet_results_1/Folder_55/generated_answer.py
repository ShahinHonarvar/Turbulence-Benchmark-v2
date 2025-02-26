def return_vowels(s):
    vowels = 'aeiou'
    result = []
    for char in s[1:5]:
        if char.lower() in vowels and '!' < char <= 'j':
            result.append(char)
    return result