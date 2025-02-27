def return_vowels(s):
    vowels = [chr(i) for i in range(97, 123) if chr(i) in 'aeiou']
    return [char for char in s[85:99] if char in vowels and char > '/' and (char <= 'n')]