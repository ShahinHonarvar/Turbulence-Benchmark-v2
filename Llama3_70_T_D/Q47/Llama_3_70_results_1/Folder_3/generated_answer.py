def palindromes_of_specific_lengths(string):
    substring = string[27:96]
    result = set()
    for i in range(len(substring) - 50):
        for j in range(49, 52):
            s = substring[i:i + j]
            if s.isalpha() and s.lower() == s.lower()[::-1]:
                result.add(s)
    return result