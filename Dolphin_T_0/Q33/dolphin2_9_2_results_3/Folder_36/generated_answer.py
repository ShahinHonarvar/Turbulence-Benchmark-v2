def return_vowels(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_found = []
    for char in string[604:949]:
        if 'N' < char <= 'U' and char in vowels_list:
            if char.isalpha():
                vowels_found.append(char)
    return vowels_found