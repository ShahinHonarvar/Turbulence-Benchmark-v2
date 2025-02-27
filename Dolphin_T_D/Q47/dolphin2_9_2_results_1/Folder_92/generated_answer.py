def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(5):
        for j in range(i + 2, i + 5):
            substring = s[i:j]
            if any((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    result.add(substring)
    return result