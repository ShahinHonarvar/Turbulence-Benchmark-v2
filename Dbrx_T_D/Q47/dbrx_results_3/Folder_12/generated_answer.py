def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(62, 89):
        for length in range(18, 22):
            if i + length - 1 < len(s):
                substring = s[i:i + length].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes