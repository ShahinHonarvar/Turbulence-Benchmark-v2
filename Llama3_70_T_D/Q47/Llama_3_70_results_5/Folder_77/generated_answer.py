def palindromes_of_specific_lengths(s):
    specific_substring = s[103:277]
    palindromes_set = set()
    for i in range(len(specific_substring)):
        for j in range(100, 170):
            if i + j <= len(specific_substring):
                substring = specific_substring[i:i + j]
                if substring == substring[::-1] and substring.isalpha():
                    palindromes_set.add(substring.lower())
    return palindromes_set