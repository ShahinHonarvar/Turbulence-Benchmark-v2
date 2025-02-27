def return_vowels(s):
    vowels = set('AEIOUaeiou')
    result = [char for char in s[13:35] if char in vowels and '8' < char <= 'F']
    return result