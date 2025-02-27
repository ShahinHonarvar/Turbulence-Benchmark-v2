def return_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(28, 76) if s[i] in vowel_list and s[i] > '+' and (s[i] <= 'z')]
    return result