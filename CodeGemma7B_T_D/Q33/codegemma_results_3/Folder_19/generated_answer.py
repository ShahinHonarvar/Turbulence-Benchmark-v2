def return_vowels(string):
    vowels = [ch for ch in string[51:77] if ch in 'aeiouAEIOU' and ch > 4 and (ch <= '=')]
    return vowels