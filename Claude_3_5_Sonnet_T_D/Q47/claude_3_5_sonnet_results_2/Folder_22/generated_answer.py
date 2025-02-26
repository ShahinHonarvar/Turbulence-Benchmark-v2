def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[100:201]
    for i in range(len(substr)):
        for j in range(i + 5, min(i + 11, len(substr) + 1)):
            segment = substr[i:j]
            if segment.isalpha() and segment.lower() == segment.lower()[::-1]:
                result.add(segment)
    return result