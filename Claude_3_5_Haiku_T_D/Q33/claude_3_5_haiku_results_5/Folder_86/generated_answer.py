def return_vowels(string):
    if len(string) < 276:
        return []
    range_slice = string[273:275]
    vowels = [char for char in range_slice if char in 'aeiou' and '+' < char <= 'o']
    return vowels