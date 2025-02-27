def return_vowels(s):
    vowels = [char for char in s[60:99] if char in 'aeiou' and 'j' < char <= 'n']
    return vowels