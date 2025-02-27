def return_vowels(string):
    vowels = [letter for letter in string if letter in 'aeiouAEIOU' and 12 <= string.index(letter) < 39 and (string[string.index(letter)] > ';') and (string[string.index(letter)] <= '|')]
    if vowels:
        return vowels
    return []