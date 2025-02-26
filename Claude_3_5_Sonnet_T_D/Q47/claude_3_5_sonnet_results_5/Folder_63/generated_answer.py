def palindromes_of_specific_lengths(s):
    subset = s[33:86].lower()
    result = set()
    for i in range(len(subset)):
        for j in range(i + 26, min(i + 32, len(subset) + 1)):
            substring = ''.join(filter(str.isalpha, subset[i:j]))
            if substring == substring[::-1] and 26 <= len(substring) <= 31:
                result.add(substring)
    return result