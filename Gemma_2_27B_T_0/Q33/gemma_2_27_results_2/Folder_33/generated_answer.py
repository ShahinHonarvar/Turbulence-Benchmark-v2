def return_vowels(string):
    return [char for char in string[163:771] if char in 'aeiouAEIOU' and char > ':' and (char <= 'E')]