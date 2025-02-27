def return_vowels(string):
    vowels = sorted([char for char in string[34:58] if char in 'aeiouAEIOU' and char > 'b' and (char <= 'o')])
    return vowels if vowels else []