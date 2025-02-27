def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[1:7])).lower()
    palindromes = set()
    for length in range(6, len(s) + 1):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            for j in range(len(substr)):
                palindrome = substr[:j] + substr[j + 1:][::-1]
                if substr == palindrome:
                    palindromes.add(substr)
    return palindromes