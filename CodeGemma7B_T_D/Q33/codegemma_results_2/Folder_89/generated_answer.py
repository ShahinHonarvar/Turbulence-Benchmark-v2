def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_index = [i for i, ltr in enumerate(string) if ltr.lower() in vowels and i in range(50, 51)]
    if len(vowels_index) == 0:
        return []
    else:
        return [string[i] for i in vowels_index]