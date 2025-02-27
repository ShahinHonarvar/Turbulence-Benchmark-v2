def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in vowels if text.index(char) in range(12, 39) and char > ';' and (char <= '|')]