def return_vowels(string):
    vowels = 'aeiouAEIOU'
    start = 20
    end = 41
    result = [letter for letter in string[start:end] if letter in vowels and 'K' < letter <= 'Z']
    return result