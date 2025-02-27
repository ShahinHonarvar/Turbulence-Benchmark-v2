def return_vowels(s):
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    result = []
    for char in s:
        if 32 <= ord(char) < 61 and char > '?' and (char <= 'P') and (char in vowels):
            result.append(char)
    return result