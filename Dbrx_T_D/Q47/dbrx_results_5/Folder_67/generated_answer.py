def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(26, 34):
        for start_index in range(65, 100 - length):
            substring = s[start_index:start_index + length]
            if len(substring) != len(set(substring).intersection(english_letters)):
                continue
            substring = substring.lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes