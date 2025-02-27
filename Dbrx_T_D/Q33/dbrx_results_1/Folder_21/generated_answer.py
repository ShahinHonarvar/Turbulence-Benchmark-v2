def return_vowels(s):
    vowels = ['a', 'e', 'i', 'og']
    return [char for char in s[463:574] if char in vowels and char > 'a' and (char <= 'g')]