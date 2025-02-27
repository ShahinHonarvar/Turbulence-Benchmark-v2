def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [ch for i, ch in enumerate(s[19:32]) if ch in vowels and '0' < ch <= '7']