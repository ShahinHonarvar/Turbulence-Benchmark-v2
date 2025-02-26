def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    if len(text) >= 852:
        for index in range(770, 852):
            char = text[index].lower()
            if char in vowels and 'b' < char <= 'i':
                result.append(text[index])
    return result