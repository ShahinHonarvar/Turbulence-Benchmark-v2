def return_vowels(s):
    vowels = [chr(i) for i in range(48, 61) if chr(i) in 'AEIOUaeiou' and '9' < chr(i) <= 'O']
    return [char for char in s if char in vowels]