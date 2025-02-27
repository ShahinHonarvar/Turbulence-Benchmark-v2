def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [char for char in s if 32 <= ord(char) < 97 and char in vowels and ('Q' < char <= ']')]
    return result