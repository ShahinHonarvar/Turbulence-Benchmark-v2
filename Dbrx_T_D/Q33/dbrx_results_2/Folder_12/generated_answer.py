def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[13:37]:
        if char > 'Z' and char <= '}' and (char in vowels):
            result.append(char)
    return result