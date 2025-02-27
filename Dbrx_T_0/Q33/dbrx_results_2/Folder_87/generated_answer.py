def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    return [char for char in s[34:58] if char > 'b' and char <= 'o' and (char in vowels)]