def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(2, 9):
        for j in range(3, 5):
            if i + j <= 9:
                substring = string[i:i + j]
                if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                    palindromes.add(substring)
    return palindromes