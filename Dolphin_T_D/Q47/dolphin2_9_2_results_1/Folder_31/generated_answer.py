def palindromes_of_specific_lengths(s):
    palindromes = set()
    available_substring = s[10:84]
    for length in range(37, 61):
        for i in range(len(available_substring) - length + 1):
            substring = available_substring[i:i + length]
            if all((char.isalpha() or char.isspace() for char in substring)):
                if substring.lower() == substring[::-1].lower():
                    palindromes.add(substring)
    return palindromes