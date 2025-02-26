def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[44:100]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 43, len(substring) + 1)):
            segment = substring[i:j]
            if segment.isalpha() and segment.lower() == segment.lower()[::-1]:
                result.add(segment)
    return result