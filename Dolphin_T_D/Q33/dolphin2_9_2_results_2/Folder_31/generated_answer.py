def return_vowels(text):
    vowels = 'aeiou'
    return [text[i] for i in range(65, 70) if text[i] in vowels and text[i] > '%' and (text[i] <= 'G')]