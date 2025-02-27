def return_vowels(string):
    vowels = 'aeiouAEIOU'
    return [char for char in string[71:81] if char > string and char <= 'U' and (char in vowels)]