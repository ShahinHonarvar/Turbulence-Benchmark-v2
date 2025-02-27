def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[30:92].lower()
    for i in range(50, 54):
        for j in range(len(substring) - i + 1):
            if substring[j:j + i] == substring[j:j + i][::-1] and substring[j:j + i].isalpha():
                palindromes.add(substring[j:j + i])
    return palindromes