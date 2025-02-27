def return_vowels(s):
    vowels = [chr(i) for i in range(41, 91) if chr(i) in 'AEIOUaeiou' and 'A' < chr(i) <= 'x']
    return [char for char in s if char in vowels]