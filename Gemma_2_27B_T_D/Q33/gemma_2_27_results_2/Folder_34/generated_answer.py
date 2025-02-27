def return_vowels(string):
    return [char for char in string[19:32] if char in 'aeiouAEIOU' and 0 < ord(char) <= 7]