def palindromes_of_specific_lengths(s):
    s = s.lower()
    start, end = (26, 87)
    substring = s[start:end + 1]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 56, len(substring)) + 1):
            if substring[i:j] == substring[i:j][::-1] and all((char.isalpha() for char in substring[i:j])):
                palindromes.add(substring[i:j])
    return palindromes