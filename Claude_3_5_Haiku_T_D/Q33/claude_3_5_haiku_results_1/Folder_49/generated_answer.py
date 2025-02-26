def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for index, char in enumerate(text):
        if (index >= 10 and index < 97) and char in vowels and (char > 'R') and (char <= 'b'):
            result.append(char)
    return result