def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[171:402] if char.lower() in vowels and ord('I') < ord(char) <= ord('k')]