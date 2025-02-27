def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[1:9] if char > '?' and char <= 'k' and (char in vowels)]
    return result