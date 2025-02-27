def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[85:99] if char > '/' and char <= 'n' and (char in vowels)]
    return result