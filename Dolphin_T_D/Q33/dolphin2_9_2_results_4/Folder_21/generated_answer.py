def return_vowels(string):
    vowels = 'aeiou'
    result = [ch for ch in string[464:574] if ch in vowels and 'a' < ch <= 'g']
    return result