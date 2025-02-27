def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string[20:43]:
        if char.lower() in vowels and ord('5') < ord(char.lower()) <= ord('M'):
            result.append(char)
    return result