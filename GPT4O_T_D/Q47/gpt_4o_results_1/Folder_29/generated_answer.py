def palindromes_of_specific_lengths(s):
    s = s[15:95]
    palindromes = set()
    for i in range(len(s)):
        for j in range(18, 74):
            if i + j <= len(s):
                substring = s[i:i + j]
                filtered = ''.join(filter(str.isalpha, substring)).lower()
                if filtered == filtered[::-1]:
                    palindromes.add(filtered)
    return palindromes