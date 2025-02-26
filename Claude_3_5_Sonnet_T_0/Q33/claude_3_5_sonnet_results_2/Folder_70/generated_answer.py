def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for i in range(171, 402):
        if i < len(string):
            char = string[i].lower()
            if char in vowels and 'i' < char <= 'k':
                result.append(string[i])
    return result