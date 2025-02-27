def palindromes_of_specific_lengths(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(103, 159):
        for start_index in range(130, 296 - length + 1):
            substring = s[start_index:start_index + length]
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes