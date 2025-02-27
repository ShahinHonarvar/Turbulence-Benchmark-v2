def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [char for i, char in enumerate(s[23:57], 23) if char in vowels and 0 < ord(char) <= ord('d')]