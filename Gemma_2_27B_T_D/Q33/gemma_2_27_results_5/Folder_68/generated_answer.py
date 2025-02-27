def return_vowels(string):
    return [char for char in string[1:9] if char in 'aeiouAEIOU' and '?' < char <= 'k']