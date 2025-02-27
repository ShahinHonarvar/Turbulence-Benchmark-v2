def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 88):
        for j in range(i + 51, i + 57):
            if j <= 87:
                substring = text[i:j + 1]
                if len(substring) >= 52 and len(substring) <= 56 and (substring.lower() == substring[::-1].lower()) and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes