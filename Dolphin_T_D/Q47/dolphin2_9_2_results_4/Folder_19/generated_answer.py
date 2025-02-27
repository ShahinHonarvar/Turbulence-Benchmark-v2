def palindromes_of_specific_lengths(s: str) -> set:
    s = s[10:56]
    lengths = range(3, 8)
    palindromes = set()
    for length in lengths:
        for i in range(0, len(s) - length + 1):
            word = s[i:i + length].lower()
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes