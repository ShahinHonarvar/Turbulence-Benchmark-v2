def palindromes_of_specific_lengths(s):
    substr = s[29:99]
    palindromes = set()
    for length in range(6, 10):
        for i in range(len(substr) - length + 1):
            segment = substr[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment.lower())
    return palindromes