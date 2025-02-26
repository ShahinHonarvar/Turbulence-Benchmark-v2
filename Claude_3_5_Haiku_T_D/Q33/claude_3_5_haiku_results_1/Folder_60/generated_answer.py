def return_vowels(string):
    vowels = 'aeiouAEIOU'
    selected_vowels = [char for char in string[24:59] if char in vowels and 'N' < char <= 'U']
    return selected_vowels