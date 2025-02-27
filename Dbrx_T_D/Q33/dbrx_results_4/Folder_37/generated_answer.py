def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[82:90] if char.lower() in vowels and 'T' < char.lower() <= 'b']
    return result