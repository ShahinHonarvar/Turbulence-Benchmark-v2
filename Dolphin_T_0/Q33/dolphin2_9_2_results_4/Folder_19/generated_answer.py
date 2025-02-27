def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = s[51:77]
    vowel_list = [char for char in substring.lower() if char in vowels and char > '4' and (char <= '=')]
    return vowel_list