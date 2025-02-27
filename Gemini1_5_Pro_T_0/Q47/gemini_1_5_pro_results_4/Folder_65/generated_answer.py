def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i, 96):
            if j - i + 1 >= 20 and j - i + 1 <= 66:
                substring = text[i:j + 1]
                if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes