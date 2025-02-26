def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for index in range(464, 574):
        if index < len(string):
            char = string[index]
            if char.lower() in vowels and 'a' < char.lower() <= 'g':
                result.append(char)
    return result