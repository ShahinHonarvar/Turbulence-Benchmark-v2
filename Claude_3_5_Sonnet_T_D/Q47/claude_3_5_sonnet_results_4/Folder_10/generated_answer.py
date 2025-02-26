def palindromes_of_specific_lengths(s):
    substring = s[16:61]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 16, min(i + 40, len(substring) + 1)):
            segment = substring[i:j]
            if segment.isalpha() and segment.lower() == segment.lower()[::-1]:
                result.add(segment)
    return result