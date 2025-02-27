from collections import defaultdict

def palindromes_of_specific_lengths(s):
    """
    :type s: str
    :rtype: set[str]
    """
    palindromes = set()
    for i in range(27, 96):
        for l in range(49, 52):
            for k in range(0, (l - 6) // 2):
                if i + k >= len(s) or i - k - l + 6 < 0 or s[i + k].lower() != s[i - k - l + 6].lower():
                    break
            else:
                palindromes.add(s[i - k - l + 6:i + k + 1])
    return palindromes