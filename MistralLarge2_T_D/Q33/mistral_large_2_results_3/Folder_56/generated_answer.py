def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for ch in s[15:86] if ch in vowels and '@' < ch <= '~']