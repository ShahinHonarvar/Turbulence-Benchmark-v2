def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[:101]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 16, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                result.add(substr)
    return result