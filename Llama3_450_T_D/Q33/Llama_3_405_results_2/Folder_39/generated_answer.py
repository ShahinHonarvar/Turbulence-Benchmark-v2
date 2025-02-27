def return_vowels(s):
    vowels = [chr(i) for i in range(32, 97) if chr(i) in 'AEIOUaeiou' and 'Q' < chr(i) <= ']']
    return [char for char in s if char in vowels]