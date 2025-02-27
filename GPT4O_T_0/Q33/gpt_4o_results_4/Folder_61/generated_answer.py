def return_vowels(s):
    return [char for char in s[1:4] if char in 'AEIOUaeiou' and 'C' < char <= 'I']