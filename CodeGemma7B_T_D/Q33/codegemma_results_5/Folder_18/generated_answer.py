def return_vowels(str_param):
    vowels = 'aeiouAEIOU'
    vowels_in_range = [ch for ch in vowels if ord(ch) >= ord('M') and ord(ch) <= ord('X') and (str_param[528:].find(ch) >= 0) and (str_param[528:].find(ch) <= 606)]
    if vowels_in_range:
        return vowels_in_range
    else:
        return []