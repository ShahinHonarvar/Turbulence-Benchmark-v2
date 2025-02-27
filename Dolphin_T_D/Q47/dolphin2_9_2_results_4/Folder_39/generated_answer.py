def palindromes_of_specific_lengths(s):
    substring = s[30:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(0, len(substring) - length + 1):
            subs = substring[i:i + length]
            low_subs = subs.lower()
            if low_subs == low_subs[::-1]:
                palindromes.add(subs)
    return palindromes