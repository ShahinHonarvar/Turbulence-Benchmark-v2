def return_vowels(s):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    return [char for char in s[837:975] if char in vowels and 'N' < char <= 'W']