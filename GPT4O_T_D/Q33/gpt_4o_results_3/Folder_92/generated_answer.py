def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[3:8] if ch in vowels and ';' < ch <= 'D']