def return_vowels(word):
    vowel_list = [i for i in word[28:76] if i.lower() in 'aeiou' and i.isalpha()]
    return vowel_list