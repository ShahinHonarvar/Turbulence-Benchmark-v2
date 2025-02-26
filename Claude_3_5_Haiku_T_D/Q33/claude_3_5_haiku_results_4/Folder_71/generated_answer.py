def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[36:56] if char in vowels and '+' < char <= '/']
    return result