def palindromes_of_specific_lengths(s):
    substring = s[:5].lower()
    lengths = set(range(3, 5))
    palindromes = []
    for start in range(len(substring) - 2):
        for length in lengths:
            if start + length > len(substring):
                break
            sub = substring[start:start + length]
            if len(set(sub)) == len(sub) and sub == sub[::-1]:
                palindromes.append(sub)
    return set(palindromes)