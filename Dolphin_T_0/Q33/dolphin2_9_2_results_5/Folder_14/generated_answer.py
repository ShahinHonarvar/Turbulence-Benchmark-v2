def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(47, 61) if 9 < ord(s[i]) <= ord('O') and s[i] in vowels]
    return result or []