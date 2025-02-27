def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[10:83]:
        if char > '%' and char <= 'e' and (char in vowels):
            result.append(char)
    return result