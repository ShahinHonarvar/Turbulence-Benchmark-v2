def return_vowels(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels = []
    for letter in string:
        if letter in vowels_list and 21 <= string.index(letter) <= 23 and (letter not in vowels):
            vowels.append(letter)
    if vowels == []:
        return []
    return vowels