def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s[70:76] if char in vowels and char > s[2] and (char <= ':')]
    return result