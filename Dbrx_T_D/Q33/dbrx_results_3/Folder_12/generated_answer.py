def return_vowels(string):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Ø', 'ø', 'Æ', 'æ', 'Å', 'å']
    return [char for char in set(string[13:37]) & set(vowels) if 'Z' < char <= '}']