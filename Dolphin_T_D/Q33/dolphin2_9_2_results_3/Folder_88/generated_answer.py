def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[70:76] if char.lower() in vowels and char > '2' and (char <= ':')]