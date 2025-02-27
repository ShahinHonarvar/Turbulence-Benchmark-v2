def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(23, 57) if s[i] > '0' and s[i] <= 'd' and (s[i] in vowels)]
    return result