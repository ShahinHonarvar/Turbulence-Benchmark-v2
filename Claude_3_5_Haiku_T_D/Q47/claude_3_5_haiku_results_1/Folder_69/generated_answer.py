def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:97].lower()
    for length in range(45, 53):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result