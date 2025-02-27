def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in string[171:402] if char in vowels and 'i' < char <= 'k']
    return result