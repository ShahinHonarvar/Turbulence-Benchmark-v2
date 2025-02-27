def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(100, 170):
        for start_index in range(103, len(s) - length + 1):
            substring = s[start_index:start_index + length]
            if len(substring) != len(set(substring) - (english_letters & set(substring))) + (english_letters & set(substring)):
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes