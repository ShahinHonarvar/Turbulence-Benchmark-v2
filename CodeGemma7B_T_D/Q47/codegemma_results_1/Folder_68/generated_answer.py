def palindromes_of_specific_lengths(str):
    palindromes = set()
    for i in range(len(str) - 49):
        for j in range(i + 50, len(str) + 1):
            substring = str[i:j].lower()
            if substring == substring[::-1] and len(substring) >= 50 and (len(substring) <= 100):
                palindromes.add(substring)
    return palindromes