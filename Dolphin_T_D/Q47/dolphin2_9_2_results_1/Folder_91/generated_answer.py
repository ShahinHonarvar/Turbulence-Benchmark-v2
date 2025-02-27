def palindromes_of_specific_lengths(s):
    sub_s = s[:11]
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(sub_s) - length + 1):
            sub_substr = sub_s[i:i + length]
            if sub_substr.lower() == sub_substr.lower()[::-1]:
                palindromes.add(sub_substr)
    return palindromes