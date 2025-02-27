def return_vowels(string):
    return [char for char in string[13:37] if char in 'aeiouAEIOU' and 'Z' < char <= '}']