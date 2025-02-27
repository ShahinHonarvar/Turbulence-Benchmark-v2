def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[19:32]:
        if char > '0' and char <= '7' and (char in vowels):
            result.append(char)
    return result