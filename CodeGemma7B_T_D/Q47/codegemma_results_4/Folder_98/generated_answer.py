def palindromes_of_specific_lengths(str):
    pattern = '[a-z]{5,80}'
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 4, min(i + 81, len(str))):
            substring = str[i:j]
            if substring == substring[::-1] and re.fullmatch(pattern, substring):
                palindromes.add(substring)
    return palindromes