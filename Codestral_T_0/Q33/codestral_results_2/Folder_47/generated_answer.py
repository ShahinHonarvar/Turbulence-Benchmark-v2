def return_vowels(s, N='N', k='k'):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[23:38] if char in vowels and N < char <= k]