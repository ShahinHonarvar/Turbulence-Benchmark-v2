def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(23, 75) if s[i] in vowels and 'L' < s[i] <= 'd']
    return result