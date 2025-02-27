def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(323, 526) if '+' < s[i] <= ':' and s[i] in vowels]