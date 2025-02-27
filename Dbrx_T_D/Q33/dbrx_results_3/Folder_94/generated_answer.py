def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[40:94]:
        if char > '4' and char <= 'H' and (char in vowels):
            result.append(char)
    return result