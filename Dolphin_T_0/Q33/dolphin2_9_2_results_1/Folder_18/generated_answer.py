def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(528, 606) if s[i] in vowels and (s[i] > 'M' and s[i] <= 'X' or (s[i] > 'm' and s[i] <= 'x'))]
    return result