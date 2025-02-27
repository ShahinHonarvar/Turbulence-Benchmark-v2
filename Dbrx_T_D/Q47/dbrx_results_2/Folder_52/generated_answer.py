def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    possible_palindromes = set()
    for i in range(44, 100):
        for j in range(13, 43):
            if i + j <= len(input_string):
                substring = input_string[i:i + j].lower()
                if len(set(substring) - english_letters) == 0:
                    if substring == substring[::-1]:
                        possible_palindromes.add(substring)
    return possible_palindromes