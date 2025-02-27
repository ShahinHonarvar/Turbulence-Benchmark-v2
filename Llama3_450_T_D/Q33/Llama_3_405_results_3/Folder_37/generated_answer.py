def return_vowels(s):
    vowels = [char for char in s if char.isalpha() and char.lower() in 'aeiou' and (82 <= ord(char) < 90) and ('T' < char <= 'b')]
    return vowels