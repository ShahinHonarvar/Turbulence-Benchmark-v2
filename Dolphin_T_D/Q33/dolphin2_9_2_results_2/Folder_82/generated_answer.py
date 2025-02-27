def return_vowels(s):
    lst = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(86, 99) if s[i] in lst and s[i] > 'e' and (s[i] <= 'r')]
    return result