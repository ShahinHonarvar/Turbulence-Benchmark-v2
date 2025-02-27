def return_vowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [v for v in vowels if x[171:402].lower().index(v) >= 0 and x[171:402].lower().index(v) <= 22 and (v > 'I') and (v <= 'k')]
    return filtered_vowels