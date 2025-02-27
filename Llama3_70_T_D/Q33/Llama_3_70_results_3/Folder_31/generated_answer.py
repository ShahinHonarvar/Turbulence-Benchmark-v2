def return_vowels(s):
    vowels = [chr(i) for i in range(65, 70) if chr(i) > '%' and chr(i) <= 'G' and (chr(i) in 'AEIOU')]
    return [char for char in s if char in vowels]