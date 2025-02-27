def return_vowels(s):
    vowels = [char for char in s[171:402] if 'I' < char <= 'k' and char in 'aeiou']
    return vowels