def return_vowels(text):
    return [x for x in text[133:306] if x in 'aeiouAEIOU' and x > 'c' and (x <= 'd')]