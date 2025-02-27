def return_vowels(s):
    vowels = [chr(i) for i in range(65, 70) if chr(i) in 'AEIOU']
    result = [char for char in s if char in vowels and '%' < char <= 'G']
    return result