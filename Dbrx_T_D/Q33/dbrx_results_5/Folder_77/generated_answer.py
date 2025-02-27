def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[837:975] if char.lower() in vowels and 'N' < char.lower() <= 'w']