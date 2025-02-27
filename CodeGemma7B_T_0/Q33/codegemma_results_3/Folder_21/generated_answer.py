def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[464:574] if char in vowels and 'a' < char <= 'g']