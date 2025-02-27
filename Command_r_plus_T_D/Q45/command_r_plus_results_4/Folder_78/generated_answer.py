def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    substring = s[6:9]
    substring = ''.join(filter(str.isalpha, substring))
    substring = substring.lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1]:
                palindromes.add(substring[i:j])
    return palindromes