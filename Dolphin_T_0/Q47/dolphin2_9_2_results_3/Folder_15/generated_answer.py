def palindromes_of_specific_lengths(s):
    s_substring = s[0:7]
    result = set()
    for length in range(3, 7):
        for i in range(len(s_substring) - length + 1):
            substring = s_substring[i:i + length]
            if all((char.isalpha() for char in substring)) and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result