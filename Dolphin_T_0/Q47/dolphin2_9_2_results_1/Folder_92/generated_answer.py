def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s[:5]
    s = s.lower()
    subsets = [s[i:i + l] for l in (3, 4) for i in range(len(s) - l + 1)]
    palindromes = {subset for subset in subsets if subset == subset[::-1]}
    return palindromes