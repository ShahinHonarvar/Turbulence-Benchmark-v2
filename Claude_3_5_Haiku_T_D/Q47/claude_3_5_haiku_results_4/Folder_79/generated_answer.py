def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[1:9]
    substring = substring.lower()
    for i in range(len(substring)):
        for length in range(3, 5):
            if i + length <= len(substring):
                candidate = substring[i:i + length]
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes