def return_vowels(string):
    vowels = [ch for ch in string[273:275] if ch > '+' and ch <= 'o' and (ch.lower() in 'aeiou')]
    return vowels