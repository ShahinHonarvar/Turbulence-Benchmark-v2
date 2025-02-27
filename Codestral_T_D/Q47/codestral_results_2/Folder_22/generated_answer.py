def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:201]
    for length in range(5, 11):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes