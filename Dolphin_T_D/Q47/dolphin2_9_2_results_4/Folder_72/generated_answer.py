def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:91]
    for length in range(27, 59):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower():
                result.add(sub)
    return result