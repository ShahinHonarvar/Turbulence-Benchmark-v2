def palindromes_of_specific_lengths(s):
    substring = s[100:296].lower()
    palindromes = set()
    n = len(substring)
    for i in range(n):
        for length in range(136, 161):
            if i + length <= n:
                candidate = substring[i:i + length]
                if candidate == candidate[::-1] and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes