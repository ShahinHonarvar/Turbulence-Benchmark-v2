def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[1:9]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            word = substring[i:j]
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes