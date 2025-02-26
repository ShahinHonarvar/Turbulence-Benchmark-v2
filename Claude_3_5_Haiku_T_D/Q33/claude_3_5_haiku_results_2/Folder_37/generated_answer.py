def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = [char for char in text[82:90] if char in vowels and 'T' < char <= 'b']
    return result