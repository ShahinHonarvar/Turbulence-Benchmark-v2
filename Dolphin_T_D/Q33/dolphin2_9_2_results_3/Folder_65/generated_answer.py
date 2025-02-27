def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(71, 88) if 9 < ord(s[i]) <= ord('P') and s[i] in vowels]
    return result