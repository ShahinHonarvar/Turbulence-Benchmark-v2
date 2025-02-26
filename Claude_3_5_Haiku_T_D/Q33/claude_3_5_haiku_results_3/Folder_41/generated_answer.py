def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[71:81] if char in vowels and 'U' >= char > '>']
    return result