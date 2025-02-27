def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in s[47:61] if char.lower() in vowels and 9 < ord(char.lower()) <= ord('o')]
    return result