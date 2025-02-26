def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(483, 664):
        if index < len(string):
            char = string[index]
            if char.lower() in vowels and '&' < char.lower() <= 'h':
                result.append(char)
    return result