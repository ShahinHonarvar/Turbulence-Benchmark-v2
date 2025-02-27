def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(21, 23) if s[i] > ' ' and s[i] <= 'n' and (s[i] in vowels)]
    return result