def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[31:92].lower()
    for i in range(len(substr)):
        for j in range(i + 50, min(i + 54, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result