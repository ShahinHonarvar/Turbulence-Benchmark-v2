def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    sub = string[529:828]
    result = [char for char in sub if char > 'U' and char <= 'l' and (char in vowels)]
    return result