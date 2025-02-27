def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = [ch for ch in s[64:82] if ch in vowels and 'P' < ch <= 'z']
    return result