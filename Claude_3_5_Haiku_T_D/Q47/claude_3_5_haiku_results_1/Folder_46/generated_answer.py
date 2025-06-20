def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[11:98].lower()
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes