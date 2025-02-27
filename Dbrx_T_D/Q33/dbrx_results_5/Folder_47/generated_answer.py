def return_vowels(s):
    vowels = [char for char in s[23:38] if char.lower() in 'aeiou' and 'N' < char <= 'k']
    return vowels