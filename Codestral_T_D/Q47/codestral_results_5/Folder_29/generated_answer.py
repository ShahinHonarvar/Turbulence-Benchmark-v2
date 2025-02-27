def palindromes_of_specific_lengths(string):
    palindromes = set()
    substr = string[15:95]
    for length in range(18, 74):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.lower() == sub.lower()[::-1]:
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes