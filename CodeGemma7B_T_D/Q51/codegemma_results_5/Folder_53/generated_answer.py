def if_contains_anagrams(str_list):
    letters_list = []
    for string in str_list:
        letters = set()
        for char in string.lower():
            if char.isalpha():
                letters.add(char)
        letters_list.append(letters)
    anagrams = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(letters_list[i]) != len(letters_list[j]):
                continue
            if len(letters_list[i]) < 3:
                continue
            if letters_list[i] == letters_list[j]:
                anagrams += 1
                if anagrams > 8:
                    return False
    return True