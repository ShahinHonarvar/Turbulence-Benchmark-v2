def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [c for c in string[90:97] if c in vowels and '_' < c <= 'x']