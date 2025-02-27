def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[24:59]:
        if char.lower() > 'n' and char.lower() <= 'u' and (char.lower() in vowels):
            result.append(char)
    return result