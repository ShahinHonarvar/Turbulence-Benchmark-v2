def return_vowels(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    return [char for char in s[77:84] if char in vowels and '(' < char <= 'G']