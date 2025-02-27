def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return [c for c in s[19:32] if c in vowels and '0' < c <= '7']