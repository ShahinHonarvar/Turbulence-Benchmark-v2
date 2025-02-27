def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 301):
        for j in range(len(string) - i + 1):
            substring = string[j:j + i]
            if substring.lower() == substring.lower()[::-1] and 30 <= len(substring) <= 300:
                palindromes.add(substring)
    return palindromes