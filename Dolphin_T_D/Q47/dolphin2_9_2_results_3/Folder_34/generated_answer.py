def palindromes_of_specific_lengths(s):
    s = s[200:301]
    palindromes = set()
    for i in range(10, 51):
        for j in range(0, len(s) - i + 1):
            substr = s[j:j + i]
            if all((ch.isalpha() for ch in substr)) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes