def return_vowels(s):
    vowels = 'EeIiOoUuYy'
    result = []
    for char in s[63:79]:
        if char in vowels and char > 'D' and (char <= 'y'):
            result.append(char)
    return result