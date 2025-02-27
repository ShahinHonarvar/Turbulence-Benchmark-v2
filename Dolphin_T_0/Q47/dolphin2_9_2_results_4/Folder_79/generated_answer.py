def palindromes_of_specific_lengths(s):
    substring = s[1:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((word.lower() == word.lower()[::-1] and word.lower().isalpha() for word in sub.split())):
                palindromes.update(sub.split())
    return palindromes