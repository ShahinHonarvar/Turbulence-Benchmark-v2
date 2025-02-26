def return_vowels(string):
    vowels = 'AEIOU'
    result = []
    for char in string:
        if char in vowels and '%' < char <= 'G' and (65 <= ord(char) < 70):
            result.append(char)
    return result