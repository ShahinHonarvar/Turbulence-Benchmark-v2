def return_vowels(text):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [char for char in text[41:50] if char in vowels and 'W' < char <= '[']
    return filtered_vowels