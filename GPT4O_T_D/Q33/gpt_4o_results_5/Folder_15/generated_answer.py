def return_vowels(s):
    vowels = 'aeiouAEIOU'
    if len(s) < 6 or ord(s[3]) >= ord('^'):
        return []
    return [char for char in s[5:6] if char in vowels and ord(s[3]) < ord(char) <= ord('^')]