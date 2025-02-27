def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return [s[i] for i in range(45, 76) if s[i] in vowels and 'b' < s[i] <= 'z']