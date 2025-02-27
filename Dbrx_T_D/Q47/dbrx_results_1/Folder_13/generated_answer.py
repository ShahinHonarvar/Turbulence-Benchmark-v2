def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(57, 61):
        for index in range(13, 96):
            if index + length > 96:
                break
            substring = string[index:index + length]
            if len(set(substring) - (set(substring) - english_letters)) == 0:
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes