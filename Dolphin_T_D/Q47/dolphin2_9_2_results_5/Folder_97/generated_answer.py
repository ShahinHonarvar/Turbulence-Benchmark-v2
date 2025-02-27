def palindromes_of_specific_lengths(s):
    s = s[27:95]
    result = set()
    for length in range(38, 50):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            if all((c.isalpha() for c in candidate)):
                if candidate.lower() == candidate[::-1].lower():
                    result.add(candidate)
    return result