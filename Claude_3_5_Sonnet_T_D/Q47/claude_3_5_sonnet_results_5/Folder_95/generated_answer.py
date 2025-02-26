def palindromes_of_specific_lengths(s):
    substring = s[12:57]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 20, i + 22):
            if j <= len(substring):
                substr = substring[i:j]
                if substr.isalpha():
                    if substr.lower() == substr.lower()[::-1]:
                        result.add(substr)
    return result