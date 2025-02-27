def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o']
    return [char for char in s[529:828] if char > 'U' and char <= 'l' and (char in vowels)]