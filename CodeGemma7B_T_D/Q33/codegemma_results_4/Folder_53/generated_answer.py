def return_vowels(text):
    string_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowel_list = []
    for char in string_vowels:
        if text.find(char) >= 27 and text.find(char) < 57 and (text.find(char) > text.find('o')) and (text.find(char) <= text.find('w')):
            vowel_list.append(char)
    return vowel_list