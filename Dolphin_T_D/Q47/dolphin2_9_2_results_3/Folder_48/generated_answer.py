def palindromes_of_specific_lengths(s):
    substring = s[155:284]
    lengths = range(104, 121)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment.lower()[::-1]:
                palindromes.add(segment)
    return palindromes