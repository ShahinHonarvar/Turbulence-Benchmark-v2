def return_vowels(string):
    vowels_list = []
    for i in range(90, 97):
        if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or (string[i] == 'o') or (string[i] == 'u'):
            if ord(string[i]) > ord('_') and ord(string[i]) <= ord('x'):
                vowels_list.append(string[i])
    if not vowels_list:
        return []
    return vowels_list