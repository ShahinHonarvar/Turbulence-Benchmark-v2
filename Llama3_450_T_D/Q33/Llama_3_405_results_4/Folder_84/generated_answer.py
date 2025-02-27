def return_vowels(s):
    vowels = [char for char in s[770:852] if char.lower() in 'aeiou' and 'B' < char <= 'i']
    return vowels