def palindromes_of_specific_lengths(s):
    substring = s[26:91]
    palindromes = set()
    length = len(substring)
    for i in range(length):
        for j in range(i + 27, min(i + 59, length + 1)):
            candidate = substring[i:j].lower()
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes