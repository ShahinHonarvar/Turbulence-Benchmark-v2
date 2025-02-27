def palindromes_of_specific_lengths(s):
    substring = s[15:87].lower()
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment == segment[::-1] and segment.isalpha():
                palindromes.add(segment)
    return palindromes