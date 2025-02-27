def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [s[i] for i in range(27, 57) if s[i] in vowels and 'o' < s[i] <= 'w']
    return result