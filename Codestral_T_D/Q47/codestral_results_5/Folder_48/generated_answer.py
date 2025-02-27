def palindromes_of_specific_lengths(string):
    substring = string[155:284]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(104, 121):
            if i + j <= len(substring):
                sub = substring[i:i + j]
                if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes