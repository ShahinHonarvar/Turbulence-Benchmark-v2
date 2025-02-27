def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [s[i] for i in range(65, 70) if s[i] in vowels and s[i] > '%' and (s[i] <= 'G')]