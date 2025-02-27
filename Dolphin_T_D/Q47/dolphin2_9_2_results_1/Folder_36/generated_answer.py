def palindromes_of_specific_lengths(string):
    substring = string[123:284]
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment.lower()[::-1]:
                palindromes.add(segment)
    return palindromes