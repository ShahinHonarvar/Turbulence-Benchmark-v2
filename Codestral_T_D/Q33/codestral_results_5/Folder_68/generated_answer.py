def return_vowels(s, q='?', k='k'):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[1:9] if char in vowels and q < char <= k]