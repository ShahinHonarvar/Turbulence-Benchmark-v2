def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for char in s[15:86] if char > '@' and char <= '~' and (char in vowels)]