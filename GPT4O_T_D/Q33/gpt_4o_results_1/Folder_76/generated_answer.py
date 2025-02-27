def return_vowels(s):
    if len(s) < 495:
        return []
    vowels = 'aeiouAEIOU'
    return [char for char in s[495:837] if char in vowels and 'B' < char <= 't']