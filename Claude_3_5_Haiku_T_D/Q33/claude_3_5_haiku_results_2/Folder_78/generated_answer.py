def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in text[46:90] if char in vowels and '@' < char <= '[']
    return result