def palindromes_of_specific_lengths(str):
    str = str[20:75]
    str = str.lower()
    str = str.replace(' ', '')
    set_of_palindromes = set()
    for i in range(len(str) - 2):
        for j in range(i + 2, len(str) - 4):
            if str[i] == str[j] and str[i + 1] == str[j - 1] and (str[i + 2] == str[j - 2]) and (str[i + 3] == str[j - 3]):
                set_of_palindromes.add(str[i:j + 1])
    for i in range(len(str) - 6):
        for j in range(i + 3, len(str) - 3):
            if str[i] == str[j] and str[i + 1] == str[j - 1] and (str[i + 2] == str[j - 2]):
                set_of_palindromes.add(str[i:j + 1])
    for i in range(len(str) - 8):
        for j in range(i + 4, len(str) - 5):
            if str[i] == str[j] and str[i + 1] == str[j - 1]:
                set_of_palindromes.add(str[i:j + 1])
    for i in range(len(str) - 10):
        for j in range(i + 5, len(str) - 7):
            if str[i] == str[j]:
                set_of_palindromes.add(str[i:j + 1])
    return set_of_palindromes