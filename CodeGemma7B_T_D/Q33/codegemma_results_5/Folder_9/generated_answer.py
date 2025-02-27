def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels[13:35] if ord(v) > 8 and ord(v) <= ord('F')]
    return filtered_vowels