def palindromes_between_indices(s):
    s = s[2:8].lower()
    chars = {c for c in s if c.isalpha()}
    palindromes = set()
    for i in range(len(chars) // 2 + 1):
        for j in range(i, len(chars) - i):
            palindrome = ''.join(sorted(chars)[i:j + 1] + list(reversed(''.join(sorted(chars))[i:j + 1])))
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes