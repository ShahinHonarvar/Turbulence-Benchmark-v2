def return_vowels(s):
    vowels = [chr(i) for i in range(47 + 1, 61) if chr(i) in 'AEIOUaeiou' and '9' < chr(i) <= 'O']
    return [c for c in s if c in vowels]