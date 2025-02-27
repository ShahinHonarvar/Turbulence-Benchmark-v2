def return_vowels(s):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    result = [ch for ch in s[11:61] if ch.upper() in vowels and 'M' < ch.upper() <= 'W']
    return result