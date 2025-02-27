def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for i, char in enumerate(s[45:76]) if char in vowels and char > 'b' and (char <= 'z')]
    return result