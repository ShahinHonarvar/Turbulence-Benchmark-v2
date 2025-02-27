def palindromes_of_specific_lengths(s):
    s = s[18:65]
    palindromes = set()
    for i in range(len(s) - 22):
        for j in range(23, min(37, len(s) - i + 1)):
            subsring = s[i:i + j]
            if subsring.lower() == subsring.lower()[::-1] and subsring.isalpha():
                palindromes.add(subsring)
    return palindromes