def return_vowels(s):
    vowels = [chr(i) for i in range(65, 91) if chr(i) in 'AEIOU']
    s = s[40:94]
    result = [char for char in s if char in vowels and char > chr(4) and (char <= 'H')]
    return result