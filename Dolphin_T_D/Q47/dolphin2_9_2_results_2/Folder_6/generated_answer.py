def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    result = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            segment = substring[i:i + length]
            if segment.lower() == segment[::-1].lower():
                result.add(segment)
    return result