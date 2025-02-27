def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_list = list(string)
    filtered_vowels = [vowels[str_list.index(v)] for v in vowels if 46 <= str_list.index(v) <= 49]
    return filtered_vowels if filtered_vowels else []