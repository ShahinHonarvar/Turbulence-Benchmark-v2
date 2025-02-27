def return_vowels(s):
    vowels = ['U', 'a', 'e', 'i', 'o', 'A', 'E', 'I', 'O']
    found = [c for c in s[17:65] if c in vowels and 'U' < c <= '{']
    return found