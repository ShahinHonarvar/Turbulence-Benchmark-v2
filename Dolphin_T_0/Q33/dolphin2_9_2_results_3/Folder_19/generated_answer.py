def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [s[i] for i in range(51, 77) if s[i] in vowels and 4 < ord(s[i]) <= 219]