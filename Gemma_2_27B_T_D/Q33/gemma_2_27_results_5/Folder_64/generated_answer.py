def return_vowels(string):
    return [x for x in string[1:7] if x in 'aeiouAEIOU' and x > 'F' and (x <= 'j')]