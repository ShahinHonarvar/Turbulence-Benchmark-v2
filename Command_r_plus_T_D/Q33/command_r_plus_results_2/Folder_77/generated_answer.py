def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = [v for v in s[837:975] if v in vowels and 'N' < v <= 'W']
    return result