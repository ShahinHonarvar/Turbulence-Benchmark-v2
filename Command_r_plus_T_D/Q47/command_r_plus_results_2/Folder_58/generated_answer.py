def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[124:284].lower()
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes