def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in s[70:81] if char > '>' and char <= 'U' and (char in vowels)]