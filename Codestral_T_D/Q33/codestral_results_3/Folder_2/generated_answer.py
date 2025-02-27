def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[170:645] if ch in vowels and 'E' < ch <= '~']