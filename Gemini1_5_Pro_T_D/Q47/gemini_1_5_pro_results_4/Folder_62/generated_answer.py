def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(26, 88):
        for j in range(i + 52, i + 57):
            if j > 87:
                break
            substring = text[i:j]
            if len(substring) >= 52 and len(substring) <= 56 and substring.isalpha() and (substring.lower() == substring[::-1].lower()):
                palindromes.add(substring)
    return palindromes