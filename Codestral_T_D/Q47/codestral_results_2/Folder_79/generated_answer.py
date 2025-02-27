def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[1:9]
    for i in range(len(substring)):
        for j in range(i + 3, i + 5):
            if j < len(substring):
                sub = substring[i:j + 1]
                if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes