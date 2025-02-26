def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[1:10]
    for i in range(len(substr)):
        for j in range(i + 3, min(i + 8, len(substr) + 1)):
            segment = substr[i:j]
            if segment.isalpha() and segment.lower() == segment.lower()[::-1]:
                result.add(segment)
    return result