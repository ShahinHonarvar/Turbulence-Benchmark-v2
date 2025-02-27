def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[529:828]:
        if char > 'U' and char <= 'l' and (char.lower() in vowels):
            result.append(char)
    return result