def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [char for char in string[171:402] if char in vowels and 'I' < char <= 'k']
    return result