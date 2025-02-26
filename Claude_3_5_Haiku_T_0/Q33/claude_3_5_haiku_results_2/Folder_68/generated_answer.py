def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[1:9] if char in vowels and '?' < char <= 'k']
    return result