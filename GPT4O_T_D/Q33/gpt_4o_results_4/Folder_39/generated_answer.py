def return_vowels(s):
    vowels = 'aeiouAEIOU'
    start, end = (32, 97)
    result = [ch for ch in s[start:end] if ch in vowels and 'Q' < ch <= ']']
    return result