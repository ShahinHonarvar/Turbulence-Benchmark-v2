def return_vowels(string_arg):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowels_in_range = [letter for letter in vowels if ord(letter) > ord('b') and ord(letter) <= ord('z') and (string_arg.index(letter) >= 45) and (string_arg.index(letter) < 76)]
    return vowels_in_range