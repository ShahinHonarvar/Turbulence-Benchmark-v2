def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:78]
    for i in range(len(substring)):
        for j in range(i + 18, min(i + 20, len(substring) + 1)):
            segment = substring[i:j]
            if segment.isalpha():
                if segment.lower() == segment.lower()[::-1]:
                    result.add(segment)
    return result