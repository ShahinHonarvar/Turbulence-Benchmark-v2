def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[15:86] if char in vowels and char > '@' and (char <= '~')]