def return_vowels(text):
    if text[3:9] == 'U':
        return ['U']
        return []
    elif text[3:9] == 's':
        return []
    vowels = ['A', 'E', 'I', 'O', 'U']
    filtered_vowels = [char for char in vowels if text[3:9] > char >= 'S']
    return filtered_vowels