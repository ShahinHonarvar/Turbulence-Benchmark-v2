def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(328, 455) if s[i] in vowels and '>' < s[i] <= 'z']
    return result