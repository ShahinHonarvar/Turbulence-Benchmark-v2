def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    substring = s[23:83]
    substring = ''.join(filter(str.isalpha, substring))
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1]:
                valid_palindromes.add(candidate)
    return valid_palindromes