def return_vowels(vowels):
    all_vowels = list(filter(lambda x: x in 'aeiouAEIOU', vowels))
    filtered_vowels = [v for v in all_vowels if v in string.ascii_lowercase and (v >= 'h' and v <= 'z')]
    return filtered_vowels