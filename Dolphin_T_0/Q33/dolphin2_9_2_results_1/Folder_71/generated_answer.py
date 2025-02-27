def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[36:56]:
        if char > '+' and char <= '/' and (char.lower() in vowels):
            result.append(char)
    return result