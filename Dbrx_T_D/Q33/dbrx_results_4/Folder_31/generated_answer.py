def return_vowels(s):
    vowels = [char for char in s if 65 <= ord(char) < 70 and char.lower() > '%' and (char.lower() <= 'g')]
    return vowels