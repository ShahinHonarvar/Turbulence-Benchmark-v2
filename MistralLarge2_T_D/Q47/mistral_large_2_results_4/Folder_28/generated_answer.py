def palindromes_of_specific_lengths(string):
    substring = string[32:72].lower()
    palindromes = set()
    for length in range(21, 33):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes