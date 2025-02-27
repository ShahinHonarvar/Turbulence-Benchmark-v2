def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return_list = []
    for char in vowels:
        if text.find(char) >= 1 and text.find(char) <= 7 and (char > 'F') and (char <= 'j'):
            return_list.append(char)
    return return_list