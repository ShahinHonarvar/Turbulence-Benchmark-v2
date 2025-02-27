def return_vowels(s):
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[41:50]:
        if char > 'W' and char <= '[' and (char in vowels):
            result.append(char)
    return result