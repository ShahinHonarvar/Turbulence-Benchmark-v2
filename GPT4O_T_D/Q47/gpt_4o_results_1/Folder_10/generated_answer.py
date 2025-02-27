def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:61].lower()
    alphabet_only = ''.join(filter(str.isalpha, substring))
    n = len(alphabet_only)
    for start in range(n):
        for length in range(16, 40):
            if start + length <= n:
                candidate = alphabet_only[start:start + length]
                if candidate == candidate[::-1]:
                    result.add(alphabet_only[start:start + length])
    return result