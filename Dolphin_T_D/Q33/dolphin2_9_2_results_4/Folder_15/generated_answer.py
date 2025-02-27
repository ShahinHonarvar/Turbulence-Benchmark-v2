def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(5, 6) if i > 3 and s[i] <= '^' and (s[i] in vowels)]
    return result