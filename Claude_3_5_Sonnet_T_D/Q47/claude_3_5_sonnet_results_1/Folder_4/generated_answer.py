def palindromes_of_specific_lengths(s):
    subset = s[12:93].lower()
    result = set()
    for i in range(len(subset)):
        for j in range(i + 17, min(i + 67, len(subset) + 1)):
            substring = subset[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result