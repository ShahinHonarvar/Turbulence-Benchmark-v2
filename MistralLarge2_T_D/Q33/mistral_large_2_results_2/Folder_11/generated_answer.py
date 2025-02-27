def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = []
    for char in s[29:73]:
        if '#' < char <= '(' and char in vowels:
            result.append(char)
    return result