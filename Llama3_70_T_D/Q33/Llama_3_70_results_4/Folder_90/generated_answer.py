def return_vowels(s):
    vowels = [char for char in s[142:145] if 'a' < char <= 'o' and char in 'aeiou']
    return vowels