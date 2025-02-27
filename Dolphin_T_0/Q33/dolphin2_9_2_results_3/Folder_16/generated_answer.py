def return_vowels(s, c, d):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [char for char in s[133:306] if char >= c and char <= d and (char in vowels)]