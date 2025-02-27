def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[14:95]
    for length in range(20, 67):
        for i in range(len(substring)):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1] and substring[i:i + length].isalpha():
                result.add(substring[i:i + length])
    return result