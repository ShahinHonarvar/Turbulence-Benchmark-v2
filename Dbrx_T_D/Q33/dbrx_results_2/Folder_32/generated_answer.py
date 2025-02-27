def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[45:76]:
        if char > 'b' and char <= 'z' and (char in vowels):
            result.append(char)
    return result