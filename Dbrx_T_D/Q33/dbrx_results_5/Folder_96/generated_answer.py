def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[77:84] if char > '(' and char <= 'G' and (char in vowels)]
    return result