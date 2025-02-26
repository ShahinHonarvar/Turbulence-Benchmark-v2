def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(1, 7):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'f' < char <= 'j':
                result.append(char)
    return result