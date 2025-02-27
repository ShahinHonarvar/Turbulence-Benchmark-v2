def palindromes_of_specific_lengths(s):
    substring = s[11:98]
    palindromes = set()
    for length in range(29, 63):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.lower().isalpha():
                palindromes.add(sub)
    return palindromes