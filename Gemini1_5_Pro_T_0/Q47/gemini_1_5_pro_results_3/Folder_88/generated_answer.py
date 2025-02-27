def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 87 - 3):
        for length in range(4, 6):
            if i + length <= 87:
                substring = text[i:i + length].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes