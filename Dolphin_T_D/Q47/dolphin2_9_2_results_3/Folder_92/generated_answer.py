def palindromes_of_specific_lengths(s):
    substring = s[:5]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if all((ch.isalpha() for ch in sub)):
                if sub.lower() == sub.lower()[::-1] and 3 <= len(sub) <= 4:
                    palindromes.add(sub)
    return palindromes