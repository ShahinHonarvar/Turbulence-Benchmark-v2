def palindromes_of_specific_lengths(s):
    substring = s[34:91].lower()
    palindromes = set()
    for length in range(14, 40):
        for start in range(len(substring) - length + 1):
            segment = substring[start:start + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes