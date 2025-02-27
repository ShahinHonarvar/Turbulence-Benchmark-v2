def return_vowels(s):
    vowels = [chr(i) for i in range(65, 91) if chr(i) in 'AEIOU']
    return [char for char in s if char in vowels and 'P' < char <= 'z']