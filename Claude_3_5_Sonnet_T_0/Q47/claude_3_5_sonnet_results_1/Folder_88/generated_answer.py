def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:88]
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                substr = substring[i:j]
                if substr.isalpha():
                    if substr.lower() == substr.lower()[::-1]:
                        result.add(substr)
    return result