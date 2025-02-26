def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:88]
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                substr = substring[i:i + length]
                if substr.isalpha():
                    if substr.lower() == substr.lower()[::-1]:
                        result.add(substr)
    return result