def return_vowels(string):
    return [char for char in string[171:402] if char in 'aeiouAEIOU' and char > 'I' and (char <= 'k')]