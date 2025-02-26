def palindromes_of_specific_lengths(s):
    substring = s[63:71]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                substr = substring[i:j]
                if substr.isalpha():
                    if substr.lower() == substr.lower()[::-1]:
                        result.add(substr)
    return result