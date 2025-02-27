def palindromes_of_specific_lengths(s: str) -> set[str]:
    s = s[123:284].lower()
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(s) - length):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes