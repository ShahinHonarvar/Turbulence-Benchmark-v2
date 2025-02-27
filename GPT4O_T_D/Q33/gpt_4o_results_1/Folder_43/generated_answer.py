def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[22:82] if ch in vowels and 'N' < ch <= 'o']