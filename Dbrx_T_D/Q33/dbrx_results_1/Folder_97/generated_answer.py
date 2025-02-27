def return_vowels(string):
    vowels = [letter for letter in string[328:455] if 'a' <= letter <= 'z' and letter in 'aeiou']
    return vowels