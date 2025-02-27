def palindromes_of_specific_lengths(string):
    result = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(12, 19):
        for index in range(29, 97 - length + 1):
            substring = string[index:index + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                result.add(substring)
    return result