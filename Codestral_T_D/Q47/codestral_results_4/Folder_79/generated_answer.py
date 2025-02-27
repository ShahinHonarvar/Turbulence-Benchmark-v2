def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[1:9]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1]:
                if substr.isalpha():
                    palindromes.add(substr)
    return palindromes