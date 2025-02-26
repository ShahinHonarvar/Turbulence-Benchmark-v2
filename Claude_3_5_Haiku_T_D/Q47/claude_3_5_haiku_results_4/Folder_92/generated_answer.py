def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:5].lower()
    for i in range(len(substring) - 2):
        for length in range(3, 5):
            if i + length > len(substring):
                break
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes