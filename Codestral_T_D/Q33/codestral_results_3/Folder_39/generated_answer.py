def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(32, 97):
        if i < len(string) and 'Q' < string[i] <= ']' and (string[i].lower() in vowels):
            result.append(string[i])
    return result