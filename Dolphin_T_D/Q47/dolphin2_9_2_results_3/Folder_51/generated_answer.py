def palindromes_of_specific_lengths(s):
    substring = s[2:9]
    result = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].lower() == substring[i:i + length].lower()[::-1] and substring[i:i + length].isalpha():
                result.add(substring[i:i + length])
    return result