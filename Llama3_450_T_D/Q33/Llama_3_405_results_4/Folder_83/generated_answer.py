def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s if char in vowels and 90 <= ord(char) < 97 and ('_' < char <= 'x')]