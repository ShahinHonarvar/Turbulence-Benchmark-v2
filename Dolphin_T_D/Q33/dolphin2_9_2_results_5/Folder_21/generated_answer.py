def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in s[464:574]:
        if char.lower() in vowels and 'a' < char.lower() <= 'g':
            result.append(char)
    return result