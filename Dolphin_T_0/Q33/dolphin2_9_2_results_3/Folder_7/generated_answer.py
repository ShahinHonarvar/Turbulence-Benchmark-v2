def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [s[i] for i in range(202, 872) if 4 < ord(s[i]) <= ord('>') and s[i] in vowels]
    return result