def return_vowels(text):
    vowels = 'aeiou'
    return_list = [i for i in text[34:69] if i > '_' and i <= 'o' and (i in vowels)]
    return return_list